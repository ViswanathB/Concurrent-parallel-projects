#!/bin/bash

counter=0
sent_count=0
done_count=0
while [ $counter -lt 10000 ]; do
	echo started $counter && \
		let sent_count=sent_count+1 &&\
		curl --location --request GET "http://127.0.0.1:5000/home" &> /dev/null \
		--header "Content-Type: text/plain" \
		--data-raw "Hi, how are you? $counter" && \
		let done_count=done_count+1
		echo sent_count:$sent_count, done_count:$done_count &
	let counter=counter+1
done
