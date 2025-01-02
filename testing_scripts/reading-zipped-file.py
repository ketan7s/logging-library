import gzip

with gzip.open('test_sync.1.log.gz', 'rt') as f:
    content = f.read()
    print(content)
