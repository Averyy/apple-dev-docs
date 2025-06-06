# keyAESearchText

**Framework**: Core Services  
**Kind**: data

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```swift
var keyAESearchText: AEKeyword { get }
```

#### Discussion

Identifies an optional parameter to the `opendocuments` Apple event, described in [`Event ID Constants`](apple_events/1527223-event_id_constants.md). The parameter contains the search text from the Spotlight search that identified the documents to be opened. The application should make a reasonable effort to display an occurrence of the search text in each opened document—for example by scrolling the text into view.

For more information, see Handling Apple Events Sent by the Mac OS in Responding to Apple Events in Apple Events Programming Guide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/keyaesearchtext)*