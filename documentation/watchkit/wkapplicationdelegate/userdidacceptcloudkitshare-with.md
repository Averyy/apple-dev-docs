# userDidAcceptCloudKitShare(with:)

**Framework**: WatchKit  
**Kind**: method

Tells the delegate that the app has access to shared information in CloudKit.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor
optional func userDidAcceptCloudKitShare(with cloudKitShareMetadata: CKShareMetadata)
```

#### Discussion

Use this method to respond to a CloudKit Sharing invitation. In your implementation, accept the share by scheduling a [`CKAcceptSharesOperation`](https://developer.apple.com/documentation/CloudKit/CKAcceptSharesOperation) object that contains the provided metadata object. After the user accepts the share, you can begin fetching records and incorporating the resulting data into your app.

The system launches the app, as necessary, before calling this method.

## Parameters

- `cloudKitShareMetadata`: Information about the CloudKit data that is available to the app. Use this object to retrieve information about the   object and the associated records that are available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/userdidacceptcloudkitshare(with:))*