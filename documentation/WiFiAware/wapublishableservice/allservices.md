# allServices

**Framework**: Wi-Fi Aware  
**Kind**: property

A dictionary of all publishable services declared by your app, indexed by service name.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
static var allServices: [WAPublishableService.ID : WAPublishableService] { get }
```

## Mentions

- [Adopting Wi-Fi Aware](adopting-wi-fi-aware.md)

#### Discussion

The system populates the contents of this property from the values under the `Info.plist` key “`WiFiAwareServices`”,  with all entries that specify the `Publishable` configuration included.

You can select a service from this property using the `serviceName` as the key to pull elements from the dictionary, or by using an extension as follows:

```swift
// Index into the dictionary.
let myService = WAPublishableService.allServices["_example-service._tcp"]!

// Give the service a symbol name.
extension WAPublishableService {
	public static var exampleService : WAPublishableService {
		allServices["_example-service._tcp"]!
	}
}
let myService = .exampleService
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapublishableservice/allservices)*