# cloudKitShareMetadata

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Information about the CloudKit data that’s now available to the app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var cloudKitShareMetadata: CKShareMetadata? { get }
```

```objc
@property (nonatomic, readonly, nullable) CKShareMetadata * cloudKitShareMetadata;
```

#### Discussion

If an invitation to share CloudKit data is available at scene-connection time, this property contains the metadata you use to accept that invitation. Use the information in the object to create and schedule a [`CKAcceptSharesOperation`](../../../CloudKit/ckacceptsharesoperation.md) object. After your operation object finishes successfully, you can begin fetching records and incorporating the resulting data into your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/connectionoptions/cloudkitsharemetadata)*