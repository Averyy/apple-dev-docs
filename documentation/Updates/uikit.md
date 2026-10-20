# UIKit updates

**Framework**: Updates  
**Role**: Article

Learn about important changes to UIKit.

#### Overview

Browse notable changes in [UIKit](../UIKit/UIKit.md).

#### September 2026

##### Arrangement view controllers

- Arrange primary and secondary view controllers using an adaptive layout that responds to the environment with [`UIArrangementViewController`](../UIKit/uiarrangementviewcontroller.md).
- Assign a view controller to the primary or secondary view of an arrangement using [`setViewController(_:for:animated:)`](../UIKit/uiarrangementviewcontroller/setviewcontroller%28_,for,animated%29.md) with a [`UIArrangementViewController.ViewPlacement`](../UIKit/uiarrangementviewcontroller/viewplacement.md).
- Update the arrangement a view controller uses, such as a split or overlay arrangement, using [`updateArrangement(_:animated:)`](../UIKit/uiarrangementviewcontroller/updatearrangement%28_,animated%29.md).
- Create a custom arrangement by conforming to [`UIArrangementViewController.Arrangement`](../UIKit/uiarrangementviewcontroller/arrangement.md), providing [`defaultViewProperties`](../UIKit/uiarrangementviewcontroller/arrangement/defaultviewproperties.md), and implementing [`setViewProperties(_:for:)`](../UIKit/uiarrangementviewcontroller/arrangement/setviewproperties%28_,for%29.md) to configure how each view appears within the arrangement.
- Look up the view controller for a view placement using [`viewController(for:)`](../UIKit/uiarrangementviewcontroller/viewcontroller%28for%29.md), get its state (including z-index, split axis, and visibility) using [`state(for:)`](../UIKit/uiarrangementviewcontroller/state%28for%29.md), and find the placement for a view controller using [`placement(for:)`](../UIKit/uiarrangementviewcontroller/placement%28for%29.md).
- Split views on one or more axes using [`UISplitArrangement`](../UIKit/uisplitarrangement-swift.struct.md) and restrict which axes the split can use with [`axes(_:)`](../UIKit/uisplitarrangement-swift.struct/axes%28_%29.md). Configure the minimum, preferred, and maximum size of a view within the split using [`UISplitArrangement.DimensionRange`](../UIKit/uisplitarrangement-swift.struct/dimensionrange.md), specifying each size as an absolute, fractional, automatic, or intrinsic [`UISplitArrangement.Dimension`](../UIKit/uisplitarrangement-swift.struct/dimension.md) value.
- Overlay views using [`UIOverlayArrangement`](../UIKit/uioverlayarrangement-swift.struct.md), and use [`axes(_:)`](../UIKit/uioverlayarrangement-swift.struct/axes%28_%29.md) to restrict the axes on which the overlay can transition to a side-by-side layout.
- Find the nearest ancestor arrangement view controller from a descendant view controller using its [`arrangementViewController`](../UIKit/uiviewcontroller/arrangementviewcontroller.md) property.

##### Reserved regions

- Identify and avoid a region of a view reserved by hardware, such as a camera or the hinge, using [`UIView.ReservedRegion`](../UIKit/uiview/reservedregion.md).
- Query the reserved regions that intersect a view using the [`reservedRegions(kind:options:)`](../UIKit/uiview/reservedregions%28kind,options%29.md) method, specifying a [`UIView.ReservedRegion.Kind`](../UIKit/uiview/reservedregion/kind-swift.struct.md) such as `.occlusion` or `.division`.
- Include inactive reserved regions in a query using the [`includeInactive`](../UIKit/uiview/reservedregion/queryoptions/includeinactive.md) option.

##### Hinge

- Observe the state of the hinge associated with a view’s hierarchy by adding a [`UIHingeInteraction`](../UIKit/uihingeinteraction.md) to the view. The interaction’s handler receives a [`UIHingeInteraction.Update`](../UIKit/uihingeinteraction/update.md) with the current hinge, or `nil` when the interaction leaves a hierarchy that provides hinge updates.
- Read the hinge’s current angle and status, such as `.closed`, `.partiallyOpen`, or `.fullyOpen`, using [`UIHinge`](../UIKit/uihinge.md).

##### Controls on the vertical axis

- Opt a view controller out of showing bar content on the vertical axis, or let the system decide, using [`preferredVerticalBarBehavior`](../UIKit/uiviewcontroller/preferredverticalbarbehavior.md) and the [`UIVerticalBarBehavior`](../UIKit/uiverticalbarbehavior.md) values `automatic` and `disabled`.
- Defer a view controller’s preference for showing bar content on the vertical axis to one of its descendants using [`childForPreferredVerticalBarBehavior`](../UIKit/uiviewcontroller/childforpreferredverticalbarbehavior.md), and signal that the preferred configuration has changed with [`setNeedsUpdateOfVerticalBarConfiguration()`](../UIKit/uiviewcontroller/setneedsupdateofverticalbarconfiguration%28%29.md).
- Read the edge where the system places controls on the vertical axis using [`verticalBarEdge`](../UIKit/uitraitcollection/verticalbaredge.md), which returns a [`UIVerticalBarEdge`](../UIKit/uiverticalbaredge.md) value such as `.leading` or `.trailing`. Register for changes to it using the traits from [`systemTraitsAffectingVerticalBarEdge`](../UIKit/uitraitcollection/systemtraitsaffectingverticalbaredge-475st.md).
- Reserve a layout region for bar content on a specific edge using [`bar(onEdge:extent:)`](../UIKit/uiview/layoutregion/bar%28onedge,extent%29-2tj1g.md).

##### Scene accessories

- Present content on the outer display of iPhone Duo while the device is open, the app is in the foreground, and a camera capture session is active, using [`cameraCapture(sceneConfiguration:)`](../UIKit/uisceneaccessory/cameracapture%28sceneconfiguration%29.md) on [`UISceneAccessory`](../UIKit/uisceneaccessory.md).
- Identify a scene created from a camera capture accessory registration using the [`windowCameraCaptureAccessory`](../UIKit/uiscenesession/role-swift.struct/windowcameracaptureaccessory.md) session role.

##### Bar items

- Control whether a bar button item appears on the vertical or horizontal axis using the [`axisBehavior`](../UIKit/uibarbuttonitem/axisbehavior-swift.property.md) property with a [`UIBarButtonItem.AxisBehavior`](../UIKit/uibarbuttonitem/axisbehavior-swift.enum.md) value, such as `.horizontalOnly` or `.verticalPreferred`.
- Control how bars compress when the system renders different types of bars together and space is constrained using the [`verticalBarCompressionBehavior`](../UIKit/uinavigationitem/verticalbarcompressionbehavior.md) property with a [`UIVerticalBarCompressionBehavior`](../UIKit/uiverticalbarcompressionbehavior.md) value, such as `.prefersBarItems` or `.prefersTabBar`.

#### June 2026

##### General

- Align sensor data from Core Location and Core Motion with your app’s UI orientation by setting a [`UIView`](../UIKit/uiview.md) as the body of a [`CLLocationManager`](../CoreLocation/cllocationmanager.md) or [`CMMotionManager`](../CoreMotion/cmmotionmanager.md) instance.
- Use [`UICollectionViewCompositionalLayoutSectionProvider`](../UIKit/uicollectionviewcompositionallayoutsectionprovider.md) closures as part of automatic observation tracking to automatically invalidate and update compositional layouts when observable objects change.
- Use [`UIRefreshControl`](../UIKit/uirefreshcontrol.md) and [`UIStepper`](../UIKit/uistepper.md) in Mac apps built with Mac Catalyst. These controls are now fully supported in the Mac idiom.

##### App life cycle

- Adopt the UIKit scene-based life cycle using the guidance in [Transitioning to the UIKit scene-based life cycle](../UIKit/transitioning-to-the-uikit-scene-based-life-cycle.md). Starting in iOS 27, apps built with the latest SDK must use the scene-based life cycle or they fail to launch.

##### Drag and drop

- Control drag initiation timing in gesture-rich views by configuring [`UIDragInteraction`](../UIKit/uidraginteraction.md). Use [`allowsPointerDragBeforeLiftDelay`](../UIKit/uidraginteraction/allowspointerdragbeforeliftdelay.md) to independently control when pointer-initiated drags begin.

##### Text views

- Override viewport layout methods directly in a [`UITextView`](../UIKit/uitextview.md) subclass by conforming to [`NSTextViewportLayoutControllerDelegate`](../UIKit/nstextviewportlayoutcontrollerdelegate.md).
- Register a [`UITextAttachmentViewProviderReusePolicy`](../UIKit/uitextattachmentviewproviderreusepolicy.md) on `UITextView` to retain attachment views during scrolling and editing, preventing flicker and preserving view state.
- Use [`NSTextTable`](../UIKit/nstexttable.md), [`NSTextBlock`](../UIKit/nstextblock.md), and [`NSTextTableBlock`](../UIKit/nstexttableblock.md) to represent table structures in attributed strings.
- Access paragraph text blocks using [`textBlocks`](../UIKit/nsparagraphstyle/textblocks.md).
- Use [`NSTextViewportRenderingSurface`](../UIKit/nstextviewportrenderingsurface.md) to render text in custom views and layers, and [`NSTextViewportRenderingSurfaceKey`](../UIKit/nstextviewportrenderingsurfacekey.md) to identify them for caching.

#### June 2025

##### General

- Provide seamless immersive visuals by using [`UIBackgroundExtensionView`](../UIKit/uibackgroundextensionview.md) to extend a view’s content under sidebars and inspectors.
- Apply Liquid Glass effects to views using [`UIGlassEffect`](../UIKit/uiglasseffect.md).
- Organize views together for morph animations in [`UIGlassContainerEffect`](../UIKit/uiglasscontainereffect.md).
- Add or adjust effects at the edge of a scroll view with [`UIScrollEdgeEffect`](../UIKit/uiscrolledgeeffect.md).
- Apply Liquid Glass effects to buttons with [`glass()`](../UIKit/uibutton/configuration-swift.struct/glass%28%29.md) and [`prominentGlass()`](../UIKit/uibutton/configuration-swift.struct/prominentglass%28%29.md).
- UIKit now supports Swift Observable objects. Use observable objects in [`layoutSubviews()`](../UIKit/uiview/layoutsubviews%28%29.md); then UIKit automatically invalidates and updates the UI when those objects change.
- Add a badge to a [`UIBarButtonItem`](../UIKit/uibarbuttonitem.md) with [`badge`](../UIKit/uibarbuttonitem/badge-4sz3f.md).
- Notification payloads are now strongly typed: [`NotificationCenter.MessageIdentifier`](../Foundation/notificationcenter/messageidentifier.md).

##### Menu bar in iPadOS

- Swipe from the top to reveal an iPad app’s full menu. Menus on iPad support images, submenus, inline sections, checkmarks, and more.
- Configure main menus with [`UIMainMenuSystem`](../UIKit/uimainmenusystem.md).

##### High dynamic range (HDR)

- [`UIColorPickerViewController`](../UIKit/uicolorpickerviewcontroller.md) supports picking HDR colors, with a maximum supported exposure value.
- Observe [`UITraitHDRHeadroomUsageLimit`](../UIKit/uitraithdrheadroomusagelimit-swift.struct.md) to automatically adjust HDR usage when a view with HDR content is not in focus.

#### June 2024

##### General

- Leverage automatic trait usage tracking inside key update methods such as [`layoutSubviews()`](../UIKit/uiview/layoutsubviews%28%29.md), eliminating the need for manual trait change registration and invalidation.
- Add repeat, wiggle, breathe, and rotate effects to [SF Symbols](https://developer.apple.com/sf-symbols/).
- Take advantage of enhancements to [`UIListContentConfiguration`](../UIKit/uilistcontentconfiguration-swift.struct.md), which now automatically updates to match the style of the containing list by using the new [`UIListEnvironment`](../UIKit/uilistenvironment.md) trait from the trait collection, removing the need to instantiate a configuration for a specific list style yourself.
- Opt out or restrict collaboration on certain types of data through the share sheet using [`UIActivityCollaborationMode`](../UIKit/uiactivitycollaborationmode.md).
- Select a specific week of the year in [`UICalendarView`](../UIKit/uicalendarview.md) using the new [`UICalendarSelectionWeekOfYear`](../UIKit/uicalendarselectionweekofyear.md) selection option.
- Observe, participate in, and affect the UI update process using [`UIUpdateLink`](../UIKit/uiupdatelink.md).

##### Navigation

- Showcase your app and its unique identity with a new, customizable launch design for document-based apps. In UIKit, define [`launchOptions`](../UIKit/uidocumentviewcontroller/launchoptions-swift.property.md) on your [`UIDocumentViewController`](../UIKit/uidocumentviewcontroller.md).
- Make your app’s navigation more immersive by adopting the new tab bar on iPad. If your app presents a rich hierarchy of tab items, set the  [`mode`](../UIKit/uitabbarcontroller/mode-swift.property.md) to [`UITabBarController.Mode.tabSidebar`](../UIKit/uitabbarcontroller/mode-swift.enum/tabsidebar.md) to automatically switch between the tab bar and sidebar representations. In SwiftUI, use [`sidebarAdaptable`](../SwiftUI/tabviewstyle/sidebaradaptable.md).
- Transition between views in a way that feels fluid and consistent using a systemwide zoom transition. In UIKit, configure your view controller’s [`preferredTransition`](../UIKit/uiviewcontroller/preferredtransition.md) to [`zoom(options:sourceViewProvider:)`](../UIKit/uiviewcontroller/transition/zoom%28options,sourceviewprovider%29.md). In SwiftUI, use [`zoom(sourceID:in:)`](../SwiftUI/navigationtransition/zoom%28sourceid,in%29.md).

##### Framework interoperability

- Reuse existing UIKit gesture recognizer code in SwiftUI. In SwiftUI, create UIKit gesture recognizers using [`UIGestureRecognizerRepresentable`](../SwiftUI/uigesturerecognizerrepresentable.md). In UIKit, refer to SwiftUI gestures by name using [`name`](../UIKit/uigesturerecognizer/name.md).

##### visionOS

- Support more varieties of list layouts by configuring whether section headers stretch to fill the entire width of the list or shrink to tightly hug their content. For collection views, use [`contentHuggingElements`](../UIKit/uicollectionlayoutlistconfiguration-swift.struct/contenthuggingelements-swift.property.md) on [`UICollectionLayoutListConfiguration`](../UIKit/uicollectionlayoutlistconfiguration-swift.struct.md). For table views, use [`contentHuggingElements`](../UIKit/uitableview/contenthuggingelements.md) on [`UITableView`](../UIKit/uitableview.md).
- Animate SF Symbols on visionOS using the symbol effects API and [`UIImageView`](../UIKit/uiimageview.md).
- Apply hierarchical vibrant text color to labels using [`UIColor.Prominence`](../UIKit/uicolor/prominence-swift.enum.md).
- Specify an action to perform without shifting the focus away from the keyboard using [`keyboardAction`](../UIKit/uitextinputassistantitem/keyboardaction.md).
- Push a new scene in place of an existing scene using [`UIWindowScenePushPlacement`](../UIKit/uiwindowscenepushplacement-swift.struct.md). The new scene appears in the same position as the original scene, hiding it. Closing the new scene makes the original scene reappear.

##### tvOS

- Create a unifying color theme in your app by specifying an accent color in your app’s asset catalog, which is now supported in tvOS.

#### June 2023

##### General

- Preview your views and view controllers alongside your code using the new `#Preview` Swift macro.
- Take advantage of a new view controller appearance callback, [`viewIsAppearing(_:)`](../UIKit/uiviewcontroller/viewisappearing%28_%29.md), to run code that depends on the view’s initial geometry. The system calls this method when both the view and view controller have an up-to-date trait collection, and after the superview adds the view to the hierarchy and lays it out. This method deploys back to iOS 13.
- Learn about enhancements to the trait system, which let you define custom traits for your own data, quickly change trait values throughout the view hierarchy, and register for trait changes in more flexible ways. For more information, see WWDC23 session 10057: [Unleash the UIKit trait system](https://developer.apple.com/videos/play/wwdc2023/10057/).
- Display and manage empty state consistently in your app with [`UIContentUnavailableConfiguration`](../UIKit/uicontentunavailableconfiguration-swift.struct.md), which provides new system standard styles and layouts for common empty states. Help people understand why no content is present, and when possible, provide guidance on how to add content.
- Create a powerful text experience in your app. Define richer interactions by changing the default tap or menu behavior when interacting with a text item. If you implement a custom UI for displaying text, support the redesigned text cursor by adopting the new text selection UI. Mark up text fields with additional text content types to help people fill out forms even faster. For more information, see WWDC23 session 10058: [What’s new with text and text interactions](https://developer.apple.com/videos/play/wwdc2023/10058/).
- Let people drop supported files and content onto your app icon on the Home Screen to open them in your app. To make sure your app is properly configured, verify that your `Info.plist` file specifies the file types your app supports using [`CFBundleDocumentTypes`](../BundleResources/information-property-list/cfbundledocumenttypes.md).

##### Accessibility and internationalization

- Simplify how you maintain your accessibility code with block-based setters for accessibility attributes. Make sure people receive the most important information first by specifying a default, low, or high priority for announcements. Enhance custom accessibility elements with the new toggle and zoom accessibility traits.
- Create a great text experience for international users by testing your UI in all languages. Adopt text styles to take advantage of enhancements to the font system, like improved wrapping and hyphenation for Chinese, German, Japanese, and Korean, as well as enhancements for variable line heights that improve legibility in several languages, including Arabic, Hindi, Thai, and Vietnamese. Access localized variants of symbol images by specifying a locale.

##### iPadOS

- Help people customize their Stage Manager configuration by including a larger target area for dragging windows. Leverage new resizing behavior for split view controllers to get the most out of your UI in Stage Manager.
- Support scrolling of your scroll view content with hardware keyboard shortcuts. This behavior is enabled by default, which you can override using [`allowsKeyboardScrolling`](../UIKit/uiscrollview/allowskeyboardscrolling.md).
- Simplify document management in your document-centric apps. Set your `UIDocument` subclass as the rename delegate of a navigation item to handle file renaming automatically. Build your content view controller from `UIDocumentViewController`, which provides a system default experience for managing documents: automatically configuring the title menu, sharing, drag and drop, key commands, and more. For more information, see WWDC23 session 10056: [Build better document-centric apps](https://developer.apple.com/videos/play/wwdc2023/10056/).
- Enhance the Apple Pencil experience in your iPadOS app. Give your app a sense of depth by using [`UIHoverGestureRecognizer`](../UIKit/uihovergesturerecognizer.md) to draw a preview of the stroke. Support the beautiful new inks in PencilKit, including monoline, fountain pen, watercolor, and crayon.

##### Views and controls

- Animate symbol images with new symbol effects, including bounce, pulse, variable color, scale, appear, disappear, and replace.
- Build even more performant apps with flexible layouts using collection views. Apply diffable data source snapshots and perform batch updates with even better performance. Use the [`uniformAcrossSiblings(estimate:)`](../UIKit/nscollectionlayoutdimension/uniformacrosssiblings%28estimate%29.md) dimension for compositional layouts to specify uniform size across sibling items, with smaller items increasing in size to match their largest sibling.
- Simplify spring animations by providing duration and bounce parameters for the new view animation method, [`animate(springDuration:bounce:initialSpringVelocity:delay:options:animations:completion:)`](../UIKit/uiview/animate%28springduration,bounce,initialspringvelocity,delay,options,animations,completion%29.md).
- Represent fractional progress through a page of content with page controls.
- Display and manipulate high dynamic range (HDR) images.
- Display your menu as a palette with [`displayAsPalette`](../UIKit/uimenu/options-swift.struct/displayaspalette.md) for it to appear as a row of menu elements for choosing from a collection of items.
- Take advantage of the [`UIStatusBarStyle.default`](../UIKit/uistatusbarstyle/default.md) status bar style, which now automatically chooses a light or dark appearance that maintains contrast with the content underneath it.

## See Also

### Technology and frameworks
- [Accelerate updates](./accelerate.md)
  Learn about important changes to Accelerate.
- [Accessibility updates](./accessibility.md)
  Learn about important changes to Accessibility.
- [ActivityKit updates](./activitykit.md)
  Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](./adattributionkit.md)
  Learn about important changes to AdAttributionKit.
- [App Clips updates](./appclips.md)
  Learn about important changes in App Clips.
- [App Intents updates](./appintents.md)
  Learn about important changes in App Intents.
- [AppKit updates](./appkit.md)
  Learn about important changes to AppKit.
- [Apple Intelligence updates](./apple-intelligence.md)
  Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](./applemapsserverapi.md)
  Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](./applepencil.md)
  Learn about important changes to Apple Pencil.
- [ARKit updates](./arkit.md)
  Learn about important changes to ARKit.
- [Audio Toolbox updates](./audiotoolbox.md)
  Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](./authenticationservices.md)
  Learn about important changes to AuthenticationServices.
- [AVFAudio updates](./avfaudio.md)
  Learn about important changes to AVFAudio.
- [AVFoundation updates](./avfoundation.md)
  Learn about important changes to AVFoundation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/uikit)*