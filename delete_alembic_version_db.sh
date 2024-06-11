#!/bin/bash

docker-compose exec postgres psql -h localhost -U mlops -d mlops_db -c "DELETE FROM alembic_version;"