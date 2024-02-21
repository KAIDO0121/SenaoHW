# Guide

1. Make sure you installed docker and docker desktop as GUI tool
    - iOS
        - It's recommended to install homebrew before installing docker
        - `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
        - `brew install docker`
    - Windows
        - https://docs.docker.com/desktop/install/windows-install/

2. Check if docker was installed successfully
    - `docker --version`

3. Check container status
    - `docker ps`

4. Add a .env file for your environment
    - Your .env file should contain these variables
        - `DATABASE_NAME=senaohw`
        - `DATABASE_USER=seanliao`
        - `DATABASE_PASSWORD=1234`
        - `DATABASE_HOST=my-postgres`
            - this value should match the service name inside the docker-compose.yml
        - `DATABASE_PORT=5432`

5. Run `docker compose up`

6. If this is the first time you start the services, open another terminal and run:
    - `docker compose run web python manage.py migrate`

7. To verify that the application works as expected, refer to the <a href = "https://documenter.getpostman.com/view/12313270/2sA2r9VhwW">documentation</a> and try the apis