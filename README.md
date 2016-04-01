# bigchaindb-trade-logger

Tool for logging trading data on BigchainDB

Assets are defined as trades and provided in the `data.csv` file and coverted to JSON format:
```json
{
  "ACCOUNT":  "ABC128" ,
  "ASSET":  "ORCL" ,
  "COMM":  "1000" ,
  "COMM_RATE":  "0.02" ,
  "CPTY1":  "MARQUIS" ,
  "CPTY2":  "BONY" ,
  "GROSS PRICE":  "2499000" ,
  "NET PRICE":  "25" ,
  "PRICE":  "50" ,
  "QUANTITY":  "50000" ,
  "SIDE":  "S" ,
  "TYPE":  "EQ"
}
```

These records are stored in BigchainDB and the transactions are assigned to `CPTY1`

### Usage

```bash
$ bigchaindb start &
$ python3 main.py 
```

