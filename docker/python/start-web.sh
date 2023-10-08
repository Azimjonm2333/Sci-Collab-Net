#!/bin/bash

set -euo pipefail

make collectstatic
#make loaddata

if [[ "$DJANGO_ENV" = "PRODUCTION" ]]; then
  make runserver-prod
else
  make initadmin
  make runserver-prod
fi