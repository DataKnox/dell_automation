# Automating Dell OS6 and OS10 Devices

## With pyATS

```
pip install pyats[full]
```

Pay close attention to the structure of the testbed YAML file. 

1. First, the hostname provided in testbed must EXACTLY match the hostname of the device, include case
2. Second, os must be Dell. If you want to run a command specific to OS6 or OS10 you must also specify platform.
3. In addition to specifying the platform, you must contain the custom abstraction order block.

# Browse Available Parsers for pyATS

![Dell Parsers Repo](https://github.com/DataKnox/genieparser/tree/master/src/genie/libs/parser/dell)

# Contact

- https://dataknox.dev
- https://twitter.com/data_knox
- https://youtube.com/c/dataknox