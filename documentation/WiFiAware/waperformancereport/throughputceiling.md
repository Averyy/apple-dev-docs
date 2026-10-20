# throughputCeiling

**Framework**: Wi-Fi Aware  
**Kind**: property  
**Role**: Instance Property

The highest throughput the connection is capable of under ideal conditions, given the hardware capabilities of both devices.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
let throughputCeiling: Double?
```

#### Discussion

The result is in `Mbps` and can be `nil` if the system can’t calculate it.

## See Also

### Getting the throughput metrics
- [let throughputCapacity: Double?](./throughputcapacity.md)
  The current estimated average throughput capacity of the data path, given the current radio conditions and concurrent Wi-Fi use cases.
- [var throughputCapacityRatio: Double?](./throughputcapacityratio.md)
  The current normalized ratio of the throughput capacity and throughput ceiling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waperformancereport/throughputceiling)*