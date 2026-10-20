# UIResponderStandardEditActions

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

A set of standard methods that apps can adopt to support editing.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
@MainActor
protocol UIResponderStandardEditActions : NSObjectProtocol
```

```objc
@protocol UIResponderStandardEditActions <NSObject>
```

#### Overview

Responder objects can implement the methods of this protocol to handle standard editing-related actions. For example, a [`UIEditMenuInteraction`](./uieditmenuinteraction.md) object displays the actions in an edit menu using these methods. UIKit searches the responder chain for an object that implements the appropriate method, calling the method on the first object that implements it.

## Topics

### Handling copy, cut, paste, and delete commands
- [func cut(Any?)](./uiresponderstandardeditactions/cut%28_%29.md)
  Removes the selected content and writes the data for it to the pasteboard.
- [func copy(Any?)](./uiresponderstandardeditactions/copy%28_%29.md)
  Copies the selected content to the pasteboard.
- [func paste(Any?)](./uiresponderstandardeditactions/paste%28_%29.md)
  Pastes the current contents of the pasteboard into your app’s interface.
- [func pasteAndGo(Any?)](./uiresponderstandardeditactions/pasteandgo%28_%29.md)
  Pastes the current contents of the pasteboard into your app’s interface and navigates to the entity it references.
- [func pasteAndMatchStyle(Any?)](./uiresponderstandardeditactions/pasteandmatchstyle%28_%29.md)
  Pastes the current contents of the pasteboard into your app’s interface using the text style of the target.
- [func pasteAndSearch(Any?)](./uiresponderstandardeditactions/pasteandsearch%28_%29.md)
  Pastes the current contents of the pasteboard into your app’s interface and performs a search.
- [func delete(Any?)](./uiresponderstandardeditactions/delete%28_%29.md)
  Removes the selected content from your interface.
### Handling find and replace commands
- [func find(Any?)](./uiresponderstandardeditactions/find%28_%29.md)
  Begins a search for content in your app’s interface.
- [func findNext(Any?)](./uiresponderstandardeditactions/findnext%28_%29.md)
  Finds the next match in your app’s interface.
- [func findPrevious(Any?)](./uiresponderstandardeditactions/findprevious%28_%29.md)
  Finds the previous match in your app’s interface.
- [func findAndReplace(Any?)](./uiresponderstandardeditactions/findandreplace%28_%29.md)
  Begins a search for content in your app’s interface and provides a replacement.
- [func useSelectionForFind(Any?)](./uiresponderstandardeditactions/useselectionforfind%28_%29.md)
  Begins a search for the selected content in your app’s interface.
### Handling selection commands
- [func select(Any?)](./uiresponderstandardeditactions/select%28_%29.md)
  Selects the content in your responder.
- [func selectAll(Any?)](./uiresponderstandardeditactions/selectall%28_%29.md)
  Selects all of the content in the current responder.
### Handling data commands
- [func duplicate(Any?)](./uiresponderstandardeditactions/duplicate%28_%29.md)
  Duplicates data.
- [func export(Any?)](./uiresponderstandardeditactions/export%28_%29.md)
  Exports data in different file formats or to other apps.
- [func move(Any?)](./uiresponderstandardeditactions/move%28_%29.md)
  Prompts a person to specify a new location and moves data to that location.
- [func rename(Any?)](./uiresponderstandardeditactions/rename%28_%29.md)
  Changes a title.
### Handling a print command
- [func printContent(Any?)](./uiresponderstandardeditactions/printcontent%28_%29.md)
  Tells your app to print available content.
### Handling styled text editing
- [func toggleBoldface(Any?)](./uiresponderstandardeditactions/toggleboldface%28_%29.md)
  Toggles the bold style information of the selected text.
- [func toggleItalics(Any?)](./uiresponderstandardeditactions/toggleitalics%28_%29.md)
  Toggles the italic style information of the selected text.
- [func toggleUnderline(Any?)](./uiresponderstandardeditactions/toggleunderline%28_%29.md)
  Toggles the underline style information of the selected text.
### Handling writing direction changes
- [func makeTextWritingDirectionLeftToRight(Any?)](./uiresponderstandardeditactions/maketextwritingdirectionlefttoright%28_%29.md)
  Changes the writing direction to left-to-right.
- [func makeTextWritingDirectionRightToLeft(Any?)](./uiresponderstandardeditactions/maketextwritingdirectionrighttoleft%28_%29.md)
  Changes the writing direction to right-to-left.
### Handling size changes
- [func increaseSize(Any?)](./uiresponderstandardeditactions/increasesize%28_%29.md)
  Increases the size of the current object by one unit.
- [func decreaseSize(Any?)](./uiresponderstandardeditactions/decreasesize%28_%29.md)
  Decreases the size of the current object by one unit.
### Handling other text formatting changes
- [func updateTextAttributes(conversionHandler: ([NSAttributedString.Key : Any]) -> [NSAttributedString.Key : Any])](./uiresponderstandardeditactions/updatetextattributes%28conversionhandler%29.md)
  Tells your app to update the attributes of the currently selected text.
### Instance Methods
- [func alignCenter(Any?)](./uiresponderstandardeditactions/aligncenter%28_%29.md)
- [func alignJustified(Any?)](./uiresponderstandardeditactions/alignjustified%28_%29.md)
- [func alignLeft(Any?)](./uiresponderstandardeditactions/alignleft%28_%29.md)
- [func alignRight(Any?)](./uiresponderstandardeditactions/alignright%28_%29.md)
- [func newFromPasteboard(Any?)](./uiresponderstandardeditactions/newfrompasteboard%28_%29.md)
- [func performClose(Any?)](./uiresponderstandardeditactions/performclose%28_%29.md)
- [func showWritingTools(Any)](./uiresponderstandardeditactions/showwritingtools%28_%29.md)
- [func toggleInspector(Any?)](./uiresponderstandardeditactions/toggleinspector%28_%29.md)
- [func toggleSidebar(Any?)](./uiresponderstandardeditactions/togglesidebar%28_%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [UIAccessibilityElement](./uiaccessibilityelement.md)
- [UIActionSheet](./uiactionsheet.md)
- [UIActivityIndicatorView](./uiactivityindicatorview.md)
- [UIActivityViewController](./uiactivityviewcontroller.md)
- [UIAlertController](./uialertcontroller.md)
- [UIAlertView](./uialertview.md)
- [UIApplication](./uiapplication.md)
- [UIArrangementViewController](./uiarrangementviewcontroller.md)
- [UIBackgroundExtensionView](./uibackgroundextensionview.md)
- [UIButton](./uibutton.md)
- [UICalendarView](./uicalendarview.md)
- [UICloudSharingController](./uicloudsharingcontroller.md)
- [UICollectionReusableView](./uicollectionreusableview.md)
- [UICollectionView](./uicollectionview.md)
- [UICollectionViewCell](./uicollectionviewcell.md)
- [UICollectionViewController](./uicollectionviewcontroller.md)
- [UICollectionViewListCell](./uicollectionviewlistcell.md)
- [UIColorPickerViewController](./uicolorpickerviewcontroller.md)
- [UIColorWell](./uicolorwell.md)
- [UIContentUnavailableView](./uicontentunavailableview.md)
- [UIControl](./uicontrol.md)
- [UIDatePicker](./uidatepicker.md)
- [UIDocumentBrowserViewController](./uidocumentbrowserviewcontroller.md)
- [UIDocumentMenuViewController](./uidocumentmenuviewcontroller.md)
- [UIDocumentPickerExtensionViewController](./uidocumentpickerextensionviewcontroller.md)
- [UIDocumentPickerViewController](./uidocumentpickerviewcontroller.md)
- [UIDocumentViewController](./uidocumentviewcontroller.md)
- [UIEventAttributionView](./uieventattributionview.md)
- [UIFontPickerViewController](./uifontpickerviewcontroller.md)
- [UIImagePickerController](./uiimagepickercontroller.md)
- [UIImageView](./uiimageview.md)
- [UIInputView](./uiinputview.md)
- [UIInputViewController](./uiinputviewcontroller.md)
- [UILabel](./uilabel.md)
- [UIListContentView](./uilistcontentview.md)
- [UINavigationBar](./uinavigationbar.md)
- [UINavigationController](./uinavigationcontroller.md)
- [UIPageControl](./uipagecontrol.md)
- [UIPageViewController](./uipageviewcontroller.md)
- [UIPasteControl](./uipastecontrol.md)
- [UIPickerView](./uipickerview.md)
- [UIPopoverBackgroundView](./uipopoverbackgroundview.md)
- [UIProgressView](./uiprogressview.md)
- [UIReferenceLibraryViewController](./uireferencelibraryviewcontroller.md)
- [UIRefreshControl](./uirefreshcontrol.md)
- [UIResponder](./uiresponder.md)
- [UIScene](./uiscene.md)
- [UIScrollView](./uiscrollview.md)
- [UISearchBar](./uisearchbar.md)
- [UISearchContainerViewController](./uisearchcontainerviewcontroller.md)
- [UISearchController](./uisearchcontroller.md)
- [UISearchTextField](./uisearchtextfield.md)
- [UISegmentedControl](./uisegmentedcontrol.md)
- [UISlider](./uislider.md)
- [UISplitViewController](./uisplitviewcontroller.md)
- [UIStackView](./uistackview.md)
- [UIStandardTextCursorView](./uistandardtextcursorview.md)
- [UIStepper](./uistepper.md)
- [UISwitch](./uiswitch.md)
- [UITabBar](./uitabbar.md)
- [UITabBarController](./uitabbarcontroller.md)
- [UITableView](./uitableview.md)
- [UITableViewCell](./uitableviewcell.md)
- [UITableViewController](./uitableviewcontroller.md)
- [UITableViewHeaderFooterView](./uitableviewheaderfooterview.md)
- [UITextField](./uitextfield.md)
- [UITextFormattingViewController](./uitextformattingviewcontroller.md)
- [UITextView](./uitextview.md)
- [UIToolbar](./uitoolbar.md)
- [UIVideoEditorController](./uivideoeditorcontroller.md)
- [UIView](./uiview.md)
- [UIViewController](./uiviewcontroller.md)
- [UIVisualEffectView](./uivisualeffectview.md)
- [UIWebView](./uiwebview.md)
- [UIWindow](./uiwindow.md)
- [UIWindowScene](./uiwindowscene.md)

## See Also

### Edit menus
- [class UIEditMenuInteraction](./uieditmenuinteraction.md)
  An interaction that provides edit operations using a menu.
- [protocol UIEditMenuInteractionDelegate](./uieditmenuinteractiondelegate.md)
  The methods for customizing the menu the interaction displays.
- [class UIEditMenuConfiguration](./uieditmenuconfiguration.md)
  An object containing the configuration details for the menu your app presents in response to an edit menu interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions)*