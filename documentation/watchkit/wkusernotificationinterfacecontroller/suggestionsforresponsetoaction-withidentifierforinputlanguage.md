# suggestionsForResponseToAction(withIdentifier:for:inputLanguage:)

**Framework**: WatchKit  
**Kind**: method

Returns an array of attributed strings representing the text suggestions to display during text input.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
@MainActor
func suggestionsForResponseToAction(withIdentifier identifier: String, for notification: UNNotification, inputLanguage: String) -> [String]
```

#### Return Value

An array of strings representing the text suggestions.

#### Discussion

When the user taps an action button that accepts text input, WatchKit calls this method to retrieve the text suggestions for that action. Use this method to supply any text phrases that might be appropriate for the given action. Use the `inputLanguage` parameter to fetch localized versions of the suggestions.

## Parameters

- `identifier`: The identifier associated with the registered action. You specify this identifier when registering your actions from your iOS app.
- `notification`: The notification object. Use this object to get information about the notification being displayed.
- `inputLanguage`: The language to use for the returned suggestions. The string contains a canonical language identifier that you can use to initialize an   object or look up localized versions of strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/suggestionsforresponsetoaction(withidentifier:for:inputlanguage:))*