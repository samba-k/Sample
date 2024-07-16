import panadas as pd
import platform
import yaml

r1 = platform.version()
r2 = platform.node()
r3 = platform.processor()
df = pd.DataFrame({'platform' : [r], 'version' : [r1], 'node' : [r2], 'processor' : [r3]})
data = df.to_dict(orient='records')
result = yaml.dump(data, default_flow_style=False)
print(result)


