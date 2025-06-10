# throughputCapacityRatio

**Framework**: Wi-Fi Aware  
**Kind**: property

The current normalized ratio of the throughput capacity and throughput ceiling.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
var throughputCapacityRatio: Double? { get }
```

#### Discussion

This ratio reflects the current throughput capability of the data path as a value between `0.0` and `1.0`. It provides a consistent measure of the relative capacity and health of a data path, regardless of the different hardware capabilities across devices.

## See Also

- [let throughputCeiling: Double?](waperformancereport/throughputceiling.md)
  The highest throughput the connection is capable of under ideal conditions, given the hardware capabilities of both devices.
- [let throughputCapacity: Double?](waperformancereport/throughputcapacity.md)
  The current estimated average throughput capacity of the data path, given the current radio conditions and concurrent Wi-Fi use cases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waperformancereport/throughputcapacityratio)*