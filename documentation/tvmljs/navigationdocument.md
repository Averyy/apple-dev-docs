# NavigationDocument

**Framework**: TVMLKit JS  
**Kind**: cl

A document stack that holds the individual TVML documents for a client-server app.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
interface NavigationDocument
```

#### Overview

You cannot create an instance of the `NavigationDocument` class. An instance of this class is available in the global context as `navigationDocument`.

## Topics

### Adding Documents to the Stack
- [insertBeforeDocument](navigationdocument/1627340-insertbeforedocument.md)
  Inserts a new document directly before a document currently on the stack.
- [pushDocument](navigationdocument/1627361-pushdocument.md)
  Pushes the specified document onto the stack.
- [replaceDocument](navigationdocument/1627430-replacedocument.md)
  Replaces a document on the stack with a new document.
### Overlaying Document
- [dismissModal](navigationdocument/1627446-dismissmodal.md)
  Dismisses the document displayed in modal view.
- [presentModal](navigationdocument/1627311-presentmodal.md)
  Displays the passed document on top of the current document.
### Viewing the Stack
- [documents](navigationdocument/1627303-documents.md)
  The documents currently on the stack.
### Removing Documents from the Stack
- [clear](navigationdocument/1627312-clear.md)
  Removes all documents currently on the stack.
- [popDocument](navigationdocument/1627397-popdocument.md)
  Removes the top most document from the stack.
- [popToDocument](navigationdocument/1627420-poptodocument.md)
  Removes all of the documents on the stack that are above the passed document. 
- [popToRootDocument](navigationdocument/1627382-poptorootdocument.md)
  Removes all documents from the stack except for the bottom-most document, which is the root document.
- [removeDocument](navigationdocument/1627394-removedocument.md)
  Removes the specified document from the stack.

## See Also

- [App](app.md)
  An object that provides access to—and a means to respond to—app life-cycle events.
- [UserDefaults](userdefaults.md)
  An object that contains the app's default preferences.
- [Responding to User Interaction](responding_to_user_interaction.md)
  Update onscreen information by adding event listeners to your Apple TV app.
- [EventListenerObject](eventlistenerobject.md)
  An object that communicates events and allows other objects to add themselves as listeners.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/navigationdocument)*