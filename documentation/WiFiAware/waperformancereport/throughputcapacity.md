# throughputCapacity

**Framework**: Wi-Fi Aware  
**Kind**: property

The current estimated average throughput capacity of the data path, given the current radio conditions and concurrent Wi-Fi use cases.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
let throughputCapacity: Double?
```

#### Discussion

The result is in `Mbps` and can be `nil` if the system can’t calculate the capacity.

## See Also

- [let throughputCeiling: Double?](waperformancereport/throughputceiling.md)
  The highest throughput the connection is capable of under ideal conditions, given the hardware capabilities of both devices.
- [var throughputCapacityRatio: Double?](waperformancereport/throughputcapacityratio.md)
  The current normalized ratio of the throughput capacity and throughput ceiling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waperformancereport/throughputcapacity)*