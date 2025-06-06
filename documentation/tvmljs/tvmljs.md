# TVMLKit JS

**Framework**: TVMLKit JS

Create tvOS client-server apps using web technologies to stream media and respond to events.

**Availability**:
- tvOS 10.0+

#### Overview

The TVMLKit JS framework provides you with the means to display client-server apps created with the Apple TV Markup Language (TVML) on tvOS. You use other classes in the framework to stream media and respond to events.

The TVMLKit JS framework incorporates the following standard Document Object Module classes, which are not documented here. For information on these classes, see [`World Wide Web Consortium`](https://developer.apple.comhttps://www.w3.org/TR/2004/REC-DOM-Level-3-Core-20040407/core.html#Node3-textContent).

- CharacterData
- Comment
- CustomEvent
- Document
- DocumentFragment
- DOMException
- DOMImplementation
- DOMImplementationLS
- DOMImplementationRegistry
- DOMParser
- Element
- Event
- EventException
- HTMLCollection
- LSException
- LSInput
- LSParser
- LSSerializer
- NamedNodeMap
- Node
- NodeList
- ParentNode
- ParsingElement
- Text
- XMLSerializer
- XPathEvaluator
- XPathException
- XPathExpression
- XPathResult

## Topics

### Essentials
- [Creating a Client-Server TVML App](creating_a_client-server_tvml_app.md)
  Display and navigate between TVML documents on Apple TV by retrieving and parsing information from a remote server.
### App Initialization
- [App](app.md)
  An object that provides access to—and a means to respond to—app life-cycle events.
- [UserDefaults](userdefaults.md)
  An object that contains the app's default preferences.
- [NavigationDocument](navigationdocument.md)
  A document stack that holds the individual TVML documents for a client-server app.
- [Responding to User Interaction](responding_to_user_interaction.md)
  Update onscreen information by adding event listeners to your Apple TV app.
- [EventListenerObject](eventlistenerobject.md)
  An object that communicates events and allows other objects to add themselves as listeners.
### Device Settings
- [Device](device.md)
  An object that provides information about an Apple TV and the host app installed on the device.
- [Settings](settings.md)
  An object that provides access to setting information for a device.
- [Restrictions](restrictions.md)
  An object used to retrieve rating restriction information.
### Media Playback
- [Playing Media in a Client-Server App](playing_media_in_a_client-server_app.md)
  Play media items in a client-server app using the built-in media player for TVMLKit JS.
- [Player](player.md)
  A media player that displays the UI for playing video and audio in an Apple TV client-server app.
- [Playlist](playlist.md)
  An array of media items to be played in an Apple TV client-server app.
- [MediaItem](mediaitem.md)
  A single audio or video item.
- [Slideshow](slideshow.md)
  An object used to display images on Apple TV in a slideshow format.
- [Browser](browser.md)
  An object used to configure and present a browsable full screen view.
### Element Access
- [Keyboard](keyboard.md)
  An object used to retrieve user input from search fields and text fields.
- [MenuBarDocument](menubardocument.md)
  An object used for setting and retrieving documents associated with a menu item.
### Data Storage and Retrieval
- [Binding JSON data to TVML documents](binding_json_data_to_tvml_documents.md)
  Create full-fledged TVML documents by using data binding and queries on simplified TVML files.
- [XMLHttpRequest](xmlhttprequest.md)
  An object used to retrieve data from a URL.
- [DataItem](dataitem.md)
  An object used to create observable objects from JSON objects for data binding.
- [Storage](storage.md)
  An object used to store key-value-pair information.
- [DataSource](datasource.md)
  An interface that allows the system to detect and respond to changes in your data.
- [LoadIndexesRequest](loadindexesrequest.md)
  A request created when the [`loadindexes`](datasource/datasource/3192119-loadindexes.md) event is triggered.
### Errors
- [TVError](tverror.md)
  Error codes for the TVError domain.
- [NSError](nserror.md)
  Information about an error condition, including a domain, a domain-specific error code, and application-specific information.
### Reference
- [TVMLKit JS Functions](tvmlkit_js_functions.md)
  The functions contained in this reference can be used globally in your app. They are not associated with a particular class.
### Classes
- [DOMException](domexception.md)
- [DOMImplementationLS](domimplementationls.md)
- [DOMImplementationRegistry](domimplementationregistry.md)
- [EventException](eventexception.md)
- [LSException](lsexception.md)
- [LSInput](lsinput.md)
- [LSParser](lsparser.md)
- [LSSerializer](lsserializer.md)
- [ParsingElement](parsingelement.md)
- [ViewModelLink](viewmodellink.md)
- [XPathException](xpathexception.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs)*