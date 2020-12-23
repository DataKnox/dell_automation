from genie.testbed import load
from rich import print

testbed = load("testbed.yml")


def test_os6():
    device = testbed.devices['DellOS6']
    # Connect to the device
    device.connect()
    output = device.parse("show ip interface")
    print(output)


def test_os10():
    device = testbed.devices['OS10']
    # Connect to the device
    device.connect()

    output = device.parse("show ip interface brief")
    print(output)


if __name__ == "__main__":
    test_os6()
    test_os10()
