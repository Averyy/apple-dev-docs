# userEnteredFormValues

**Framework**: Wi-Fi Infrastructure  
**Kind**: property

The user-entered form values to complete captive portal login.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
let userEnteredFormValues: [String : String]
```

#### Discussion

The dictionary content depends on the available data:

- `[:]` when no data is available, due to empty forms, no entries, expired data, or removal by the person.
- A set of key-value pairs representing the data that the person entered.

When present, the key-value pairs contain:

- : A [`CSS selector`](https://developer.apple.comhttps://www.w3.org/TR/selectors-4/) that locates the HTML element within the document, using `querySelector()` or `querySelectorAll()` functions.
- : The corresponding HTML element value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/network/captiveportallogin-swift.struct/userenteredformvalues)*