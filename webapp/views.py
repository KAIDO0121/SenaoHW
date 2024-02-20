from .models import User
from datetime import datetime,timezone
from django.contrib.auth.hashers import check_password
from rest_framework import generics, status
from rest_framework.response import Response
from .exceptions import Throttled
from .serializers import UserVerifySerializer, UserCreateSerializer
from collections import defaultdict
import heapq

class UserCreate(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):

        self.create(request, *args, **kwargs)

        return Response({"success": True, "reason": ""}, status=status.HTTP_201_CREATED)
        
class Throttler():
    counter = defaultdict(list)

    def update(self, key, curTime):
        heapq.heapify(self.counter[key])
        while self.counter[key] and curTime - self.counter[key][0] > 60:
            heapq.heappop(self.counter[key])
            
    
    def addFailTS(self, key, curTime):
        heapq.heappush(self.counter[key], curTime)
    
    def getCounter(self):
        return self.counter

class UserVerify(generics.GenericAPIView):
    throttler = Throttler()
    fails = throttler.getCounter()

    serializer_class = UserVerifySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        curts = datetime.now(timezone.utc).timestamp()
        name = request.data.get('username')
        
        if name:
            self.throttler.update(name, curts)
        
        if len(self.fails[name]) >= 5:
            raise Throttled(detail = {"reason": "Too many failed attempt", "success":False})
        
        try:
            serializer.is_valid(raise_exception=True)
            serializer.authenticate(request.data)
            self.fails[name] = []
            return Response({"success": True, "reason": ""}, status=status.HTTP_200_OK)
        except Exception as e:
            self.throttler.addFailTS(name, curts)
            return Response(e.__dict__['detail'], status=e.__dict__['status_code'])
        
            