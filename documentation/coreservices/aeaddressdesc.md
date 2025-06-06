# AEAddressDesc

**Framework**: Core Services  
**Kind**: tdef

A descriptor that contains the address of an application, used to describe the target application for an Apple event.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias AEAddressDesc = AEDesc
```

#### Discussion

An address descriptor is identical to a descriptor of data type [`AEDesc`](aedesc.md); however, the data for an address descriptor must always consist of the address of an application.

Every Apple event includes an attribute specifying the address of the target application. The address in an address descriptor can be specified as one of these types (or as any other descriptor type you define that can be coerced to one of these types): `typeApplSignature`, `typeSessionID`, or `typeProcessSerialNumber`.

These constants are described in [`Descriptor Type Constants`](apple_events/1542788-descriptor_type_constants.md).

You can also use [`typeApplicationBundleID`](https://developer.apple.com/documentation/applicationservices/apple_event_manager/1542896-typeapplicationbundleid).

If your application sends Apple events to itself using a `typeProcessSerialNumber` address descriptor with the `lowLongOfPSN` field set to `kCurrentProcess` (and the `highLongOfPSN` field set to 0), the Apple Event Manager jumps directly to the appropriate Apple event handler without going through the normal event-processing sequence. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/aeaddressdesc)*