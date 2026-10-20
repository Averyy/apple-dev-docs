# presentModal

**Framework**: TVMLKit JS  
**Kind**: instm  
**Role**: Instance Method

Displays the passed document on top of the current document.

**Availability**:
- tvOS 9.0+

## Declaration

```
void presentModal(
    in Document document
);
```

#### Discussion

The passed document is presented on top of the current document. The current document is blurred and is used as the background for the modal document.

## Parameters

- `document`: A DOM document created by parsing a TVML file.

## See Also

### Overlaying Document
- [dismissModal](./api-1627446-dismissmodal.md)
  Dismisses the document displayed in modal view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/navigationdocument/1627311-presentmodal)*