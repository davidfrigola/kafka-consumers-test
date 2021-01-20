
# Kafka POC - producer, consumers and topics

As Kafka documentation states, you can have as many consumers actively consuming from a topic, as a group, as the number of partitions you have.

This POC demonstrates it, using very simple python producer and cosumer .

# The producer

Check the code in  `producer.py`. It has an inifite loop, sending a message with a timestamp, and sleeping for 1sec.

# The consumer(s)

In `consumer.py` , you can see a consumer for the group `poc-group`, printing the messages received from the topic.

# A programatically setup

In `kafka-setup.py`, a `poc-topic` is created with 2 partitions.

# The test
Setup your environment. I use virtualenv, then pip install -r requirements.txt, and that's all.
You'll have to figure out how to spin up a local kafka broker, I use docker-compose from https://github.com/confluentinc/cp-all-in-one

Run `python kafka-setup.py`
This will create the topic `poc-topic` with 2 partitions.


Then, in a terminal, run the producer:
```
python producer.py
Message sent %s some data in bytes 1611170322.1077127
Message sent %s some data in bytes 1611170323.1272047
Message sent %s some data in bytes 1611170324.1288335
Message sent %s some data in bytes 1611170325.1305933
...
```

In 2 other terminals, run a consumer
```
python consumer.py
poc-topic:0:523: key=None value=b'some data in bytes 1611170357.2019012'
poc-topic:0:524: key=None value=b'some data in bytes 1611170358.2052937'
poc-topic:0:525: key=None value=b'some data in bytes 1611170359.2070754'
....
```

Now the interesting part ... let's add a new consumer.
It should has no effect, as partitions are already assigned to each consumer.
But the thing is that, when added, it starts  to consume messages!!
And apparently the last started consumer gets stalled.

Interesting, isn't it?
