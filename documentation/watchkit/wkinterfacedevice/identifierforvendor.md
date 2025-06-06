# identifierForVendor

**Framework**: Watchkit  
**Kind**: property

An alphanumeric string that uniquely identifies a device to the app’s vendor.

**Availability**:
- watchOS 6.2+

## Declaration

```swift
var identifierForVendor: UUID? { get }
```

#### Discussion

Use this value to validate in-app purchase receipts on a device. If the value is `nil`, you can wait and try again. For example, this property may return `nil` after the device has been restarted but before the user has unlocked it.

##### Validate Receipts

To validate the receipt, you need to calculate the SHA-1 hash of the following:  the value from the [`identifierForVendor`](wkinterfacedevice/identifierforvendor.md) property, the `Opaque Value` from the receipt, and the root bundle identifier. Concatenate these values in order as a series of bytes, and then compute the SHA-1 hash of the series.

For the `Opaque Value`, use the raw bytes from the receipt without performing any UTF-8 string interpretation or normalization. For a watchOS app with an iOS companion, the root bundle identifier is the iOS app’s bundle identifier. For a watch-only app, use the root target’s bundle identifier.

For more information on validating in-app purchases, see [`Choosing a receipt validation technique`](https://developer.apple.com/documentation/StoreKit/choosing-a-receipt-validation-technique).

##### Understand Identifier Values

The value of [`identifierForVendor`](wkinterfacedevice/identifierforvendor.md) is the same for all apps from the same vendor running on the same device. Apps on the same device from different vendors return different values, as do all apps running on different devices.

The value in this property remains the same as long as the device has the app (or another app from the same vendor) installed. The value changes when the user deletes all of a vendor’s apps from the device and subsequently reinstalls one or more of them. The value can also change when you install test builds using Xcode or when a user installs an app on a device using ad-hoc distribution. Therefore, if your app stores the value of this property anywhere, you should gracefully handle situations in which the identifier changes.

For more information on how the identifier is calculated, see the [`UIDevice`](https://developer.apple.com/documentation/UIKit/UIDevice) class’s [`identifierForVendor`](https://developer.apple.com/documentation/UIKit/UIDevice/identifierForVendor) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/identifierforvendor)*