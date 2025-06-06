# cancel

**Framework**: TVMLKit JS  
**Kind**: instp

Cancels the load request.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
attribute  cancel;
```

#### Discussion

The `cancel` event is invoked when TVMLKit wants to cancel a previous `LoadIndexesRequest`. This could happen if the indexes disappear from view, making the it unnecessary to load data for those indexes. 

Your implementation can ignore this event and still load the requested data if needed, but ideally the event should be handled to cancel any opened XHR requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/loadindexesrequest/3192158-cancel)*