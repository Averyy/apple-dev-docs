# fetchAllDataStoreIdentifiers(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Type Method

Fetches an array of identifiers from existing data stores that have identifiers.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func fetchAllDataStoreIdentifiers(_ completionHandler: @escaping @MainActor @Sendable ([UUID]) -> Void)
```

```swift
class var allDataStoreIdentifiers: [UUID] { get async }
```

```objc
+ (void) fetchAllDataStoreIdentifiers:(void (^)(NSArray<NSUUID *> *)) completionHandler;
```

## Parameters

- `completionHandler`: A block to invoke with the fetched list of unique identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/fetchalldatastoreidentifiers(_:))*