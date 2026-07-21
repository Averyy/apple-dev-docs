# SetClockDomain

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetClockDomain(uint32_t in_clock_domain);
```

#### Return Value

Returns kern_return_t

#### Discussion

Set the uint32_t clock domain value of the IOUserVideoClockDevice. A uint32_t whose value indicates the clock domain to which the IOUserVideoClockDevice belongs. IOUserVideoClockDevice’s that have the same value for this property are able to be synchronized in hardware. However, a value of 0 indicates that the clock domain for the device is unspecified and should be assumed to be separate from every other device’s clock domain, even if they have the value of 0 as their clock domain as well.

Drivers can change the clock domain  of the clock device dynamically.  A notification will be sent to the host to update the object state if successful.

## Parameters

- `in_clock_domain`: uint32_t clock domain to set

## See Also

- [GetClockDomain](iouservideoclockdevice/getclockdomain.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/setclockdomain)*