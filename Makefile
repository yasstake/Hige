

liquid-data:
	./venv/bin/python liquid/bbliquid.py > ./DATA/liquid.csv

download:
	wget -o LOG https://public.bybit.com/trading/BTCUSD/BTCUSD2021-05-14.csv.gz
	wget -o LOG https://public.bybit.com/trading/BTCUSD/BTCUSD2021-05-15.csv.gz
