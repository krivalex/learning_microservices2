from time import sleep
from logging import getLogger

logger = getLogger(__name__)

print("hello")
for i in range(10):
    logger.warning(i)
    print(i)
    sleep(1)
print("bye bye")
