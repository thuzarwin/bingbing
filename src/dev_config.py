import base64

KEY = "Byygq1zI2KKyssKp8UvVe3DV/v6Aa0FEsKrE+pqDa0s"
ID = "0c3454d3-67ce-4558-b4ac-1e95f964cdf5"
ENCODED_KEY = base64.b64encode("{0}:{1}".format(KEY, KEY))
ALPHA               = 1
BETA                = 0.75
GAMMA               = 0.15
print_str = """
-----------------------------------------
{0}) {1} ({2})
{3}
-----------------------------------------"""
