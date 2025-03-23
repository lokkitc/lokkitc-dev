up:
	docker compose -f docker-compose-local.yaml up -d

down:
	docker compose -f docker-compose-local.yaml down && docker network prune -f

stop:
	docker stop $(docker ps -q)

restart:
	docker compose -f docker-compose-local.yaml restart

delete:
	docker rm $(docker ps -a -q)

delete-images:
	docker rmi $(docker images -q)

migrate:
	PYTHONPATH=C:\Users\talim\GlobalProjects\lokkitcdev\lokkitc-dev
	alembic revision --autogenerate -m "$(message)"
	alembic upgrade head


