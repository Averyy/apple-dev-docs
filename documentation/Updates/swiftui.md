# SwiftUI updates

**Framework**: Updates  
**Role**: Article

Learn about important changes to SwiftUI.

## Overview

Browse notable changes in [SwiftUI](../SwiftUI/SwiftUI.md).

## September 2026

### Arrangement views

- Arrange primary and secondary content using an adaptive layout that responds to the environment with [`ArrangementView`](../SwiftUI/arrangementview.md).
- Configure the style of an [`ArrangementView`](../SwiftUI/arrangementview.md) using the [`arrangementViewStyle(_:)`](../SwiftUI/view/arrangementviewstyle%28_%29.md) modifier.
- Create a custom arrangement style by conforming to [`ArrangementViewStyle`](../SwiftUI/arrangementviewstyle.md) and implementing [`makeBody(configuration:)`](../SwiftUI/arrangementviewstyle/makebody%28configuration%29.md), which provides access to the arrangement’s [`primary`](../SwiftUI/arrangementviewstyleconfiguration/primary-swift.property.md) and [`secondary`](../SwiftUI/arrangementviewstyleconfiguration/secondary-swift.property.md) content.
- Place the primary and secondary views of an arrangement view side by side along one or more axes using the [`split`](../SwiftUI/arrangementviewstyle/split.md) style, and restrict which axes the split arrangement can use with [`axes(_:)`](../SwiftUI/splitarrangementviewstyle/axes%28_%29.md).
- Set the preferred or constrained size ratio for a view relative to its related view in a split arrangement using [`splitArrangementLayoutRatio(_:)`](../SwiftUI/view/splitarrangementlayoutratio%28_%29.md) or [`splitArrangementLayoutRatio(minHorizontal:idealHorizontal:maxHorizontal:minVertical:idealVertical:maxVertical:)`](../SwiftUI/view/splitarrangementlayoutratio%28minhorizontal,idealhorizontal,maxhorizontal,minvertical,idealvertical,maxvertical%29.md).
- Set size constraints for a view in a split arrangement using absolute width and height values with [`splitArrangementLayoutSize(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:)`](../SwiftUI/view/splitarrangementlayoutsize%28minwidth,idealwidth,maxwidth,minheight,idealheight,maxheight%29.md), or prefer the view’s own ideal size with [`splitArrangementFixedLayoutSize(horizontal:vertical:)`](../SwiftUI/view/splitarrangementfixedlayoutsize%28horizontal,vertical%29.md).
- Read the axis of the current split arrangement from a subview using the [`splitArrangementAxis`](../SwiftUI/environmentvalues/splitarrangementaxis.md) environment value.
- Layer the primary view over the secondary view in z-order using the [`overlay`](../SwiftUI/arrangementviewstyle/overlay.md) style, and restrict the axes on which the overlay can transition to a side-by-side layout with [`axes(_:)`](../SwiftUI/overlayarrangementviewstyle/axes%28_%29.md). Anchor the overlaid content to a specific vertical or horizontal edge with the [`overlayArrangementEdge(_:)`](../SwiftUI/view/overlayarrangementedge%28_%29.md) modifier.
- Read the z-index of a view within an overlay arrangement using the [`overlayArrangementZIndex`](../SwiftUI/environmentvalues/overlayarrangementzindex.md) environment value.

### Reserved regions

- Identify and avoid a region of a view reserved by hardware, such as a camera or the hinge, using [`ReservedRegion`](../SwiftUI/reservedregion.md).
- Query the reserved regions that intersect a view using the [`reservedRegions(kind:options:layoutDirectionBehavior:)`](../SwiftUI/geometryproxy/reservedregions%28kind,options,layoutdirectionbehavior%29.md) method, specifying a [`ReservedRegion.Kind`](../SwiftUI/reservedregion/kind-swift.struct.md) such as `.occlusion` or `.division`.
- Include inactive reserved regions in a query using the [`includeInactive`](../SwiftUI/reservedregion/queryoptions/includeinactive.md) option.
- Identify a reserved region across coordinate spaces, or track it over time, using its opaque [`ReservedRegion.ID`](../SwiftUI/reservedregion/id-swift.struct.md) identifier.

### Hinge

- Observe changes to the state of the hinge on iPhone Duo using the [`onHingeChange(isEnabled:_:)`](../SwiftUI/view/onhingechange%28isenabled,_%29.md) modifier, which delivers updates through [`DeviceHingeContext`](../SwiftUI/devicehingecontext.md).
- Read the hinge’s current angle and status, such as `.closed`, `.partiallyOpen`, or `.fullyOpen`, using [`DeviceHinge`](../SwiftUI/devicehinge.md).

### Scene accessories

- Present content on the outer display of iPhone Duo while the device is open, the app is in the foreground, and a camera capture session is active, using [`CameraCaptureAccessory`](../SwiftUI/cameracaptureaccessory.md).

### Controls on the vertical axis

- Read the edge where the system places controls on the vertical axis using the [`toolbarVerticalEdge`](../SwiftUI/environmentvalues/toolbarverticaledge.md) environment value, then position custom bars or other UI relative to the system’s placement.
- Opt a view out of showing bar content on the vertical axis, causing bar content to fall back to the standard horizontal top and bottom toolbars, using the [`toolbarVerticalBehavior(_:)`](../SwiftUI/view/toolbarverticalbehavior%28_%29.md) modifier.
- Control whether a toolbar item appears on the vertical or horizontal axis using the [`axisBehavior(_:)`](../SwiftUI/toolbarcontent/axisbehavior%28_%29.md) and [`axisBehavior(_:)`](../SwiftUI/customizabletoolbarcontent/axisbehavior%28_%29.md) modifiers with a [`ToolbarItemAxisBehavior`](../SwiftUI/toolbaritemaxisbehavior.md) value, such as `.horizontalOnly` or `.verticalPreferred`.
- Manage how bars compress when the system renders different types of bars together and space is constrained using the [`toolbarVerticalCompressionBehavior(_:)`](../SwiftUI/view/toolbarverticalcompressionbehavior%28_%29.md) modifier with a [`ToolbarVerticalCompressionBehavior`](../SwiftUI/toolbarverticalcompressionbehavior.md) value, such as `.prefersToolbarItems` or `.prefersTabBar`.

## June 2026

### General

- Build your project in Xcode 27 or later so that the `@State` attribute uses the [`State()`](../SwiftUI/state%28%29.md) macro to create a state value in an [`App`](../SwiftUI/app.md), [`Scene`](../SwiftUI/scene.md), or [`View`](../SwiftUI/view.md). This change only initializes and stores your property once when it’s a class.
- Build your project in Xcode 27 or later to construct type-agnostic content from closures that you mark with [`ContentBuilder`](../SwiftUI/contentbuilder.md), which serves as the unified replacement for type-specific builders like [`ToolbarContentBuilder`](../SwiftUI/toolbarcontentbuilder.md) and [`CommandsBuilder`](../SwiftUI/commandsbuilder.md).
- Add reordering by drag-and-drop in containers such as lists, stacks, grids, or custom layouts with [`reorderable()`](../SwiftUI/dynamicviewcontent/reorderable%28%29.md) and [`reorderContainer(for:isEnabled:move:)`](../SwiftUI/view/reordercontainer%28for,isenabled,move%29.md).
- Add custom swipe actions to views in containers such as scroll views, stacks, grids, or custom layouts using [`swipeActions(edge:allowsFullSwipe:content:onPresentationChanged:)`](../SwiftUI/view/swipeactions%28edge,allowsfullswipe,content,onpresentationchanged%29.md) and [`swipeActionsContainer()`](../SwiftUI/view/swipeactionscontainer%28%29.md).

### Transitions

- Specify the  [`crossFade`](../SwiftUI/navigationtransition/crossfade.md) transition to have a sheet appear by fading in over content.

### Images

- Cache images locally that you download with [`AsyncImage`](../SwiftUI/asyncimage.md), using [`asyncImageURLSession(_:)`](../SwiftUI/view/asyncimageurlsession%28_%29.md), [`init(request:scale:)`](../SwiftUI/asyncimage/init%28request,scale%29.md), [`init(request:scale:content:placeholder:)`](../SwiftUI/asyncimage/init%28request,scale,content,placeholder%29.md), and [`init(request:scale:transaction:content:)`](../SwiftUI/asyncimage/init%28request,scale,transaction,content%29.md).

### Toolbars

- Use the [`visibilityPriority(_:)`](../SwiftUI/toolbarcontent/visibilitypriority%28_%29.md) modifier to prioritize important toolbar actions so SwiftUI keeps them visible as space shrinks, moving lower-priority items to the overflow menu first.
- Send secondary toolbar actions, like archive or delete, directly to the overflow menu by wrapping them in a [`ToolbarOverflowMenu`](../SwiftUI/toolbaroverflowmenu.md), keeping your primary toolbar focused on key actions.
- Anchor a toolbar item to the trailing edge of the top bar using the [`topBarPinnedTrailing`](../SwiftUI/toolbaritemplacement/topbarpinnedtrailing.md) placement so it stays in place even as other items shift or move to the overflow menu.
- Control how toolbars minimize in response to scrolling using the [`toolbarMinimizationBehavior(_:for:)`](../SwiftUI/view/toolbarminimizationbehavior%28_,for%29.md) modifier.

### Documents

- Build document-based apps that read directly from a file URL by conforming your document class to [`ReadableDocument`](../SwiftUI/readabledocument.md), enabling access to large files and integration with URL-based frameworks.
- Add write support to a URL-based document by also conforming to [`WritableDocument`](../SwiftUI/writabledocument.md).
- Implement custom reading and writing logic with [`DocumentReader`](../SwiftUI/documentreader.md) and [`DocumentWriter`](../SwiftUI/documentwriter.md), or use [`FileWrapperDocumentReader`](../SwiftUI/filewrapperdocumentreader.md) and [`FileWrapperDocumentWriter`](../SwiftUI/filewrapperdocumentwriter.md) for simpler file-wrapper-based cases.
- Access the document’s file URL and last modification date, and coordinate additional file access, using [`URLDocumentConfiguration`](../SwiftUI/urldocumentconfiguration.md).
- Export a [`WritableDocument`](../SwiftUI/writabledocument.md) to disk using the [`fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:onCancellation:)`](../SwiftUI/view/fileexporter%28ispresented,document,contenttype,defaultfilename,oncompletion,oncancellation%29.md) modifier.

### Tab bars

- Set the [`prominent`](../SwiftUI/tabrole/prominent.md) role on a tab to place the tab in a separate, trailing position of the tab bar.

### Alerts and confirmation dialogs

- Present an alert or confirmation dialog from an optional data item or error object, and use that data to produce the content and title:

  - [`alert(_:item:actions:)`](../SwiftUI/view/alert%28_,item,actions%29.md)
  - [`alert(error:actions:)`](../SwiftUI/view/alert%28error,actions%29.md)
  - [`alert(_:item:actions:message:)`](../SwiftUI/view/alert%28_,item,actions,message%29.md)
  - [`alert(error:actions:message:)`](../SwiftUI/view/alert%28error,actions,message%29.md)
  - [`confirmationDialog(_:item:titleVisibility:actions:)`](../SwiftUI/view/confirmationdialog%28_,item,titlevisibility,actions%29.md)
  - [`confirmationDialog(_:item:titleVisibility:actions:message:)`](../SwiftUI/view/confirmationdialog%28_,item,titlevisibility,actions,message%29.md)

### Gestures

- Specify the sources of gesture input to recognize, such as direct or indirect touches, pencil, or pointer. The following gestures have initializers that you can use to specify the sources of gesture input: [`DragGesture`](../SwiftUI/draggesture.md), [`LongPressGesture`](../SwiftUI/longpressgesture.md), [`MagnifyGesture`](../SwiftUI/magnifygesture.md), [`RotateGesture`](../SwiftUI/rotategesture.md), [`RotateGesture3D`](../SwiftUI/rotategesture3d.md), [`SpatialEventGesture`](../SwiftUI/spatialeventgesture.md), [`SpatialTapGesture`](../SwiftUI/spatialtapgesture.md), [`TapGesture`](../SwiftUI/tapgesture.md), [`WindowDragGesture`](../SwiftUI/windowdraggesture.md). For more information see [`GestureInputKinds`](../SwiftUI/gestureinputkinds.md).

## June 2025

### General

- Apply Liquid Glass effects to views using [`glassEffect(_:in:)`](../SwiftUI/view/glasseffect%28_,in%29.md).
- Use [`glass`](../SwiftUI/primitivebuttonstyle/glass.md) with the [`buttonStyle(_:)`](../SwiftUI/view/buttonstyle%28_%29-66fbx.md) modifier to apply Liquid Glass to instances of `Button`.
- [`ToolbarSpacer`](../SwiftUI/toolbarspacer.md) creates a visual break between items in toolbars containing Liquid Glass.
- Use [`scrollEdgeEffectStyle(_:for:)`](../SwiftUI/view/scrolledgeeffectstyle%28_,for%29.md) to configure the scroll edge effect style for scroll views.
- [`backgroundExtensionEffect()`](../SwiftUI/view/backgroundextensioneffect%28%29.md) duplicates, mirrors, and blurs views placed around edges with available safe areas.
- Set behavior for tab bar minimization with [`tabBarMinimizeBehavior(_:)`](../SwiftUI/view/tabbarminimizebehavior%28_%29.md).
- Set the [`search`](../SwiftUI/tabrole/search.md) role on a tab to take someone to a search tab and have a search field take the place of the tab bar.
- Adjust the content of accessory views based on the placement in a tab view with [`TabViewBottomAccessoryPlacement`](../SwiftUI/tabviewbottomaccessoryplacement.md).
- Connect a [`WebView`](../WebKit/webview-swift.struct.md) with a [`WebPage`](../WebKit/webpage.md) to fully control the browsing experience in your app.
- Drag multiple items using the [`draggable(containerItemID:containerNamespace:)`](../SwiftUI/view/draggable%28containeritemid,containernamespace%29.md) modifier. Make a view a container for draggable views using the [`dragContainer(for:itemID:in:_:)`](../SwiftUI/view/dragcontainer%28for,itemid,in,_%29.md) modifier.
- Use the [`Animatable()`](../SwiftUI/animatable%28%29.md) macro to have SwiftUI synthesize custom animatable data properties.
- [`Slider`](../SwiftUI/slider.md) now supports tick marks. Tick marks appear automatically when initializing a `Slider` with the `step` parameter.
- Use [`windowResizeAnchor(_:)`](../SwiftUI/view/windowresizeanchor%28_%29.md) to set the window anchor point when a window must resize.

### Text

- [`TextEditor`](../SwiftUI/texteditor.md) now supports [`AttributedString`](../Foundation/attributedstring.md).
- Handle text selection with attributed text using [`AttributedTextSelection`](../SwiftUI/attributedtextselection.md).
- [`AttributedTextFormattingDefinition`](../SwiftUI/attributedtextformattingdefinition.md) defines how text can be styled in specific contexts.
- Use [`FindContext`](../SwiftUI/findcontext.md) to create a find navigator in views that support text editing.

### Accessibility

- Support Assistive Access in iOS and iPadOS scenes with [`AssistiveAccess`](../SwiftUI/assistiveaccess.md).

### HDR

- [`Color.ResolvedHDR`](../SwiftUI/color/resolvedhdr.md) is a set of RGBA values that represent a color that can be shown, including HDR headroom information.

### UIKit and AppKit integration

- Host and present SwiftUI scenes in UIKit with [`UIHostingSceneDelegate`](../SwiftUI/uihostingscenedelegate.md) and in AppKit with [`NSHostingSceneRepresentation`](../SwiftUI/nshostingscenerepresentation.md).
- Incorporate gesture recognizers in SwiftUI views from AppKit with [`NSGestureRecognizerRepresentable`](../SwiftUI/nsgesturerecognizerrepresentable.md).

### Immersive spaces

- Manipulate views using common hand gestures with [`manipulable(coordinateSpace:operations:inertia:isEnabled:onChanged:)`](../SwiftUI/view/manipulable%28coordinatespace,operations,inertia,isenabled,onchanged%29.md).
- Snap volumes to horizontal surfaces and windows to vertical surfaces using [`SurfaceSnappingInfo`](../SwiftUI/surfacesnappinginfo.md).
- Use [`RemoteImmersiveSpace`](../SwiftUI/remoteimmersivespace.md) to render stereo content from your Mac app on Apple Vision Pro.
- Use [`SpatialContainer`](../SwiftUI/spatialcontainer.md) to create a layout container that aligns overlapping content in 3D space.
- Depth-based variants of modifiers allow easier volumetric layouts in SwiftUI. For example, [`aspectRatio3D(_:contentMode:)`](../SwiftUI/view/aspectratio3d%28_,contentmode%29.md), [`rotation3DLayout(_:)`](../SwiftUI/view/rotation3dlayout%28_%29.md), and [`depthAlignment(_:)`](../SwiftUI/layout/depthalignment%28_%29.md).

## June 2024

### Volumes

- Specify the alignment of a volume when moved in the world using the [`volumeWorldAlignment(_:)`](../SwiftUI/scene/volumeworldalignment%28_%29.md) scene modifier.
- Specify the default world scaling behavior of your scene using the [`defaultWorldScaling(_:)`](../SwiftUI/scene/defaultworldscaling%28_%29.md) scene modifier.
- Adjust the visibilty of a volume’s baseplate using the [`volumeBaseplateVisibility(_:)`](../SwiftUI/view/volumebaseplatevisibility%28_%29.md) view modifier.
- Define a custom action to execute when the viewpoint of a volume changes using the [`onVolumeViewpointChange(updateStrategy:initial:_:)`](../SwiftUI/view/onvolumeviewpointchange%28updatestrategy,initial,_%29.md) view modifier.

### Windows

- Change the default initial size and position of a window using the [`defaultWindowPlacement(_:)`](../SwiftUI/scene/defaultwindowplacement%28_%29.md) modifier.
- Change the default behavior for how windows behave when performing a zoom using [`WindowIdealSize`](../SwiftUI/windowidealsize.md) and provide the placement for the zoomed window with the [`windowIdealPlacement(_:)`](../SwiftUI/scene/windowidealplacement%28_%29.md) modifier.
- Create utility windows in SwiftUI using the new [`UtilityWindow`](../SwiftUI/utilitywindow.md) scene type and toggle the window’s visibility using the [`WindowVisibilityToggle`](../SwiftUI/windowvisibilitytoggle.md).
- Customize the style of a window using the new [`window`](../SwiftUI/containerbackgroundplacement/window.md) container background placement, the [`toolbar(removing:)`](../SwiftUI/view/toolbar%28removing%29.md) view modifier, and the [`plain`](../SwiftUI/windowstyle/plain.md) window style.
- Set the default launch behavior for a scene using the [`defaultLaunchBehavior(_:)`](../SwiftUI/scene/defaultlaunchbehavior%28_%29.md) modifier.
- Replace one scene with another using the [`pushWindow`](../SwiftUI/environmentvalues/pushwindow.md) method.

### Immersive spaces

- Add an action to perform when the state of the immersion changes using the [`onImmersionChange(initial:_:)`](../SwiftUI/view/onimmersionchange%28initial,_%29.md) modifier.
- Apply a custom color or dim a passthrough video in an immersive space using the [`colorMultiply(_:)`](../SwiftUI/surroundingseffect/colormultiply%28_%29.md) and [`dim(intensity:)`](../SwiftUI/surroundingseffect/dim%28intensity%29.md) initializers.

### Documents

- Customize the launch experience of document-based applications using [`DocumentGroupLaunchScene`](../SwiftUI/documentgrouplaunchscene.md) and [`NewDocumentButton`](../SwiftUI/newdocumentbutton.md).

### Navigation

- Specify the appearance and interaction of [`TabView`](../SwiftUI/tabview.md) with the [`tabViewStyle(_:)`](../SwiftUI/view/tabviewstyle%28_%29.md)  modifier using values like [`sidebarAdaptable`](../SwiftUI/tabviewstyle/sidebaradaptable.md), [`tabBarOnly`](../SwiftUI/tabviewstyle/tabbaronly.md), and [`grouped`](../SwiftUI/tabviewstyle/grouped.md).
- Build hierarchy by nesting tabs as a tab item within [`TabSection`](../SwiftUI/tabsection.md).
- Enable people to customize a [`TabView`](../SwiftUI/tabview.md) using the [`tabViewCustomization(_:)`](../SwiftUI/view/tabviewcustomization%28_%29.md) modifier and persist customization state in [`AppStorage`](../SwiftUI/appstorage.md) with [`TabViewCustomization`](../SwiftUI/tabviewcustomization.md).

### Modal presentations

- Use built-in presentation sizes for sheets like [`form`](../SwiftUI/presentationsizing/form.md) or [`page`](../SwiftUI/presentationsizing/page.md) with the [`presentationSizing(_:)`](../SwiftUI/view/presentationsizing%28_%29.md) modifier or create custom sized sheets using the [`PresentationSizing`](../SwiftUI/presentationsizing.md) protocol.

### Toolbars

- Specify the display mode of toolbars in macOS using the [`ToolbarLabelStyle`](../SwiftUI/toolbarlabelstyle.md) type.
- Configure the foreground style in the toolbar environment in watchOS using the [`toolbarForegroundStyle(_:for:)`](../SwiftUI/view/toolbarforegroundstyle%28_,for%29.md) view modifier.
- Anchor ornaments relative to the depth of your volume — in addition to the height and width — using the [`scene(_:)`](../SwiftUI/ornamentattachmentanchor/scene%28_%29-1l8wf.md) method that takes a [`UnitPoint3D`](../SwiftUI/unitpoint3d.md).

### Views

- Create custom container views like [`Picker`](../SwiftUI/picker.md), [`List`](../SwiftUI/list.md), and [`TabView`](../SwiftUI/tabview.md) using new [`Group`](../SwiftUI/group.md) and [`ForEach`](../SwiftUI/foreach.md) initializers, like [`init(subviews:transform:)`](../SwiftUI/group/init%28subviews,transform%29.md) and [`init(subviews:content:)`](../SwiftUI/foreach/init%28subviews,content%29.md), respectively.
- Declare a custom container value by defining a key that conforms to the [`ContainerValueKey`](../SwiftUI/containervaluekey.md) protocol, and set the container value for a view using the [`containerValue(_:_:)`](../SwiftUI/view/containervalue%28_,_%29.md) modifier.
- Create [`EnvironmentValues`](../SwiftUI/environmentvalues.md), [`Transaction`](../SwiftUI/transaction.md), [`ContainerValues`](../SwiftUI/containervalues.md), and [`FocusedValues`](../SwiftUI/focusedvalues.md) entries by using the [`Entry()`](../SwiftUI/entry%28%29.md) macro to the variable declaration.

### Animation

- Customize the transition when pushing a view onto a navigation stack or presenting a view with the [`navigationTransition(_:)`](../SwiftUI/view/navigationtransition%28_%29.md) view modifier.
- Add new symbols effects and configurations like [`wiggle`](../Symbols/symboleffect/wiggle.md), [`rotate`](../Symbols/symboleffect/rotate.md), and [`breathe`](../Symbols/symboleffect/breathe.md) using the [`symbolEffect(_:options:value:)`](../SwiftUI/view/symboleffect%28_,options,value%29.md) modifier.

### Text input and output

- Add text suggestions support to any text field using [`textInputSuggestions(_:)`](../SwiftUI/view/textinputsuggestions%28_%29.md) and [`textInputCompletion(_:)`](../SwiftUI/view/textinputcompletion%28_%29.md) view modifiers.
- Access and modify selected text using a new [`TextSelection`](../SwiftUI/textselection.md) binding for [`TextField`](../SwiftUI/textfield.md) and [`TextEditor`](../SwiftUI/texteditor.md).
- Bind to the focus state of an app’s search field using the [`searchFocused(_:equals:)`](../SwiftUI/view/searchfocused%28_,equals%29.md) view modifier.

### Drawing and graphics

- Precompile shaders at build time using the [`compile(as:)`](../SwiftUI/shader/compile%28as%29.md) method.
- Create mesh gradients with a grid of points and colors using the new [`MeshGradient`](../SwiftUI/meshgradient.md) type.
- Extend SwiftUI Text views with custom rendering effects and interaction behaviors using [`TextAttribute`](../SwiftUI/textattribute.md), [`Text.Layout`](../SwiftUI/text/layout.md), and [`TextRenderer`](../SwiftUI/textrenderer.md).
- Create a new [`Color`](../SwiftUI/color.md) by mixing two colors using the [`mix(with:by:in:)`](../SwiftUI/color/mix%28with,by,in%29.md) method.

### Layout

- Enable custom spacing between views in a [`ZStack`](../SwiftUI/zstack.md) along the depth axis with the [`init(alignment:spacing:content:)`](../SwiftUI/zstack/init%28alignment,spacing,content%29.md) initializer.

### Scrolling

- Scroll to a view, offset, or edge in a scroll view using the [`scrollPosition(_:anchor:)`](../SwiftUI/view/scrollposition%28_,anchor%29.md) view modifier and specifying one of the [`ScrollPosition`](../SwiftUI/scrollposition.md) values.
- Limit the number of views that can be scrolled by a single interaction using the limit behavior value [`alwaysByFew`](../SwiftUI/viewalignedscrolltargetbehavior/limitbehavior/alwaysbyfew.md) or [`alwaysByOne`](../SwiftUI/viewalignedscrolltargetbehavior/limitbehavior/alwaysbyone.md).
- Add an action to be called when a view crosses a provided threshold using the [`onScrollVisibilityChange(threshold:_:)`](../SwiftUI/view/onscrollvisibilitychange%28threshold,_%29.md) modifier.
- Access both the old and new values when a scroll view’s phase changes by using the [`onScrollPhaseChange(_:)`](../SwiftUI/view/onscrollphasechange%28_%29-7mica.md) modifier.

### Gestures

- Conditionally disable a gesture using the `isEnabled` parameter in a modifier like [`gesture(_:isEnabled:)`](../SwiftUI/view/gesture%28_,isenabled%29.md).
- Create extra drag areas of a window in macOS when you add a [`WindowDragGesture`](../SwiftUI/windowdraggesture.md) gesture.
- Create a hand gesture shortcut for Double Tap in watchOS using the [`HandGestureShortcut`](../SwiftUI/handgestureshortcut.md) structure.
- Enable whether gestures can handle events that activate the containing window using the [`allowsWindowActivationEvents(_:)`](../SwiftUI/view/allowswindowactivationevents%28_%29.md) view modifier.

### Input events

- Create a group of hover effects that activate together using [`HoverEffectGroup`](../SwiftUI/hovereffectgroup.md) and apply them to a view using the [`hoverEffect(in:isEnabled:body:)`](../SwiftUI/view/hovereffect%28in,isenabled,body%29.md) view modifier.
- Customize the appearance of the system pointer in macOS, iPadOS, and visionOS with new pointer styles using [`pointerStyle(_:)`](../SwiftUI/view/pointerstyle%28_%29.md) or the visibility with the [`pointerVisibility(_:)`](../SwiftUI/view/pointervisibility%28_%29.md) modifier.
- Access keyboard modifier flags using the [`onModifierKeysChanged(mask:initial:_:)`](../SwiftUI/view/onmodifierkeyschanged%28mask,initial,_%29.md).
- Replace the primary view with one or more alternative views when pressing a specified set of modifier keys using the [`modifierKeyAlternate(_:_:)`](../SwiftUI/view/modifierkeyalternate%28_,_%29.md) view modifier.
- Enable the hand pointer for custom drawing and markup applications using the [`handPointerBehavior(_:)`](../SwiftUI/view/handpointerbehavior%28_%29.md) modifier.

### Previews in Xcode

- Write dynamic properties inline in previews using the new [`Previewable()`](../SwiftUI/previewable%28%29.md) macro.
- Inject shared environment objects, model containers, or other dependencies into previews using the [`PreviewModifier`](../SwiftUI/previewmodifier.md) protocol.

### Accessibility

- Specify that your accessibility element behaves as a tab bar using the [`isTabBar`](../SwiftUI/accessibilitytraits/istabbar.md) accessibility trait with the [`accessibilityAddTraits(_:)`](../SwiftUI/view/accessibilityaddtraits%28_%29.md) modifier. In UIKit, use [`tabBar`](../UIKit/uiaccessibilitytraits/tabbar.md).
- Generate a localized description of a color in a string interpolation by adding `accessibilityName:`, such as `"\(accessibilityName: myColor)"`. Pass that string to any accessibility modifier.

### Framework interoperability

- Reuse existing UIKit gesture recognizer code in SwiftUI. In SwiftUI, create UIKit gesture recognizers using [`UIGestureRecognizerRepresentable`](../SwiftUI/uigesturerecognizerrepresentable.md). In UIKit, refer to SwiftUI gestures by name using [`name`](../UIKit/uigesturerecognizer/name.md).
- Share menu content definitions between SwiftUI and AppKit by using the [`NSHostingMenu`](../SwiftUI/nshostingmenu.md) in your AppKit view hierarchy.

---

## June 2023, visionOS

### Scenes

- Create a volume that can display 3D models by applying the [`volumetric`](../SwiftUI/windowstyle/volumetric.md) window style to an app’s window.
- Make use of a Full Space by opening an [`ImmersiveSpace`](../SwiftUI/immersivespace.md) scene. You can use the [`mixed`](../SwiftUI/immersionstyle/mixed.md) immersion style to place objects in a person’s surroundings, or the [`full`](../SwiftUI/immersionstyle/full.md) style to completely control the visual experience.
- Display 3D models in a volume or a Full Space using RealityKit entities that you load with that framework’s [`Model3D`](../RealityKit/model3d.md) or [`RealityView`](../RealityKit/realityview.md) structure.

### Toolbars and ornaments

- Display a toolbar item in an ornament using the [`bottomOrnament`](../SwiftUI/toolbaritemplacement/bottomornament.md) toolbar item placement.
- Add an ornament to a window directly using the [`ornament(visibility:attachmentAnchor:contentAlignment:ornament:)`](../SwiftUI/view/ornament%28visibility,attachmentanchor,contentalignment,ornament%29.md) view modifier.

### Drawing and graphics

- Detect view geometry in three dimensions using a [`GeometryReader3D`](../SwiftUI/geometryreader3d.md).
- Add a 3D visual effect using the [`visualEffect3D(_:)`](../SwiftUI/view/visualeffect3d%28_%29.md) view modifier.
- Rotate or scale in three dimensions with view modifiers like [`rotation3DEffect(_:anchor:)`](../SwiftUI/view/rotation3deffect%28_,anchor%29.md) and [`scaleEffect(x:y:z:anchor:)`](../SwiftUI/view/scaleeffect%28x,y,z,anchor%29.md), respectively.
- Convert between display points and physical distances using a [`PhysicalMetricsConverter`](../SwiftUI/physicalmetricsconverter.md).

### View configuration

- Add a glass background effect to a view using the [`glassBackgroundEffect(displayMode:)`](../SwiftUI/view/glassbackgroundeffect%28displaymode%29.md) view modifier.
- Dim passthrough when appropriate by applying a [`preferredSurroundingsEffect(_:)`](../SwiftUI/view/preferredsurroundingseffect%28_%29.md) modifier.

### View layout

- Make 3D adjustments to layout with view modifiers like [`offset(z:)`](../SwiftUI/view/offset%28z%29.md), [`padding3D(_:)`](../SwiftUI/view/padding3d%28_%29-6bex4.md), and [`frame(depth:alignment:)`](../SwiftUI/view/frame%28depth,alignment%29.md).

### Gestures

- Enable people to rotate objects in three dimensions when you add a [`RotateGesture3D`](../SwiftUI/rotategesture3d.md) gesture.

---

## June 2023

### Scenes

- Close windows by their identifier using the [`dismissWindow`](../SwiftUI/environmentvalues/dismisswindow.md) action stored in the environment.
- Enable people to open a settings window by presenting a [`SettingsLink`](../SwiftUI/settingslink.md) button.

### Navigation

- Control views of a navigation split view or stack using a new overload of the [`navigationDestination(item:destination:)`](../SwiftUI/view/navigationdestination%28item,destination%29.md) view modifier.
- Manage column visibility of a navigation split view using new overloads of the view’s initializer, like [`init(columnVisibility:preferredCompactColumn:sidebar:content:detail:)`](../SwiftUI/navigationsplitview/init%28columnvisibility,preferredcompactcolumn,sidebar,content,detail%29.md).

### Modal presentations

- Use new overloads of the file export, import, and move modifiers, like [`fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)`](../SwiftUI/view/fileexporter%28ispresented,document,contenttypes,defaultfilename,oncompletion,oncancellation%29-34bd6.md), to access new file management features. For example, you can:

  - Configure a file import or export dialog to open on a default directory, enable only certain file types, display hidden files, and so on.
  - Retain file interface configuration that a person chooses from one presentation to the next.
  - Export types that conform to the [`Transferable`](../CoreTransferable/transferable.md) protocol.
- Specify a dialog severity using the [`dialogSeverity(_:)`](../SwiftUI/view/dialogseverity%28_%29.md) view modifier.
- Provide a custom icon for a dialog using the [`dialogIcon(_:)`](../SwiftUI/view/dialogicon%28_%29.md) modifier.
- Enable people to suppress dialogs using one of the dialog suppression modifiers, like [`dialogSuppressionToggle(isSuppressed:)`](../SwiftUI/view/dialogsuppressiontoggle%28issuppressed%29.md).

### Toolbars

- Configure the toolbar title display size using the [`toolbarTitleDisplayMode(_:)`](../SwiftUI/view/toolbartitledisplaymode%28_%29.md) modifier.

### Search

- Present search programmatically using a binding to a new `isPresented` parameter available in some searchable view modifiers, like [`searchable(text:isPresented:placement:prompt:)`](../SwiftUI/view/searchable%28text,ispresented,placement,prompt%29-1hn4y.md).
- Create mutable search tokens by providing a binding to the input of the `token` closure in the applicable searchable view modifiers, like [`searchable(text:editableTokens:isPresented:placement:prompt:token:)`](../SwiftUI/view/searchable%28text,editabletokens,ispresented,placement,prompt,token%29-2ilmg.md).

### Data and storage

- Bridge between SwiftUI environment keys and UIKit traits more easily using the [`UITraitBridgedEnvironmentKey`](../SwiftUI/uitraitbridgedenvironmentkey.md) protocol.
- Get better performance when you share data throughout your app by using the new [`Observable()`](../Observation/observable%28%29.md) macro.
- Access both the old and new values of a value that changes when processing the completion closure of the [`onChange(of:initial:_:)`](../SwiftUI/view/onchange%28of,initial,_%29-4psgg.md) view modifier.

### Views

- Display a standard interface when a resource, like search results or a network connection, isn’t available using the [`ContentUnavailableView`](../SwiftUI/contentunavailableview.md) view type.
- Display a standard inspector interface with a platform-appropriate appearance by applying the [`inspector(isPresented:content:)`](../SwiftUI/view/inspector%28ispresented,content%29.md) modifier.

### Animation

- Perform an action when an animation completes by specifying a completion closure to the [`withAnimation(_:completionCriteria:_:completion:)`](../SwiftUI/withanimation%28_,completioncriteria,_,completion%29.md) view modifier.
- Define custom animation behaviors by creating a type that conforms to the [`CustomAnimation`](../SwiftUI/customanimation.md) protocol.
- Perform animations that progress through predefined phases using the [`PhaseAnimator`](../SwiftUI/phaseanimator.md) structure, or according to a set of time-based keyframes by using the [`Keyframes`](../SwiftUI/keyframes.md) protocol.
- Specify information about a change in state — for example, to request a particular animation — using custom [`TransactionKey`](../SwiftUI/transactionkey.md) instances.
- Design custom animation curves using [`UnitCurve`](../SwiftUI/unitcurve.md).
- Apply streamlined spring parameters, now standardized across all Apple frameworks, using the new [`spring(duration:bounce:blendDuration:)`](../SwiftUI/animation/spring%28duration,bounce,blendduration%29.md) animation. You can also use the [`Spring`](../SwiftUI/spring.md) structure as a convenience to represent a spring’s motion.

### Text input and output

- Indicate the language that appears in a specific [`Text`](../SwiftUI/text.md) view so that SwiftUI can help to avoid clipping and collision of text, and perform proper line breaking and hyphenation using the [`typesettingLanguage(_:isEnabled:)`](../SwiftUI/view/typesettinglanguage%28_,isenabled%29-4ldzm.md) view modifier.
- Scale text semantically, for example by labeling it as having a secondary text scale, using the [`textScale(_:isEnabled:)`](../SwiftUI/view/textscale%28_,isenabled%29.md) modifier.

### Shapes

- Apply more than one [`fill(_:style:)`](../SwiftUI/shape/fill%28_,style%29-3y2ud.md) or [`stroke(_:style:antialiased:)`](../SwiftUI/shape/stroke%28_,style,antialiased%29.md) modifier to a single [`Shape`](../SwiftUI/shape.md).
- Apply Boolean operations to both shapes and paths, like [`intersection(_:eoFill:)`](../SwiftUI/shape/intersection%28_,eofill%29.md) and [`union(_:eoFill:)`](../SwiftUI/shape/union%28_,eofill%29.md).
- Use predefined shape styles, like [`rect`](../SwiftUI/shape/rect.md), to simplify your code.
- Create rounded rectangles with uneven corners using [`rect(topLeadingRadius:bottomLeadingRadius:bottomTrailingRadius:topTrailingRadius:style:)`](../SwiftUI/shape/rect%28topleadingradius,bottomleadingradius,bottomtrailingradius,toptrailingradius,style%29.md).

### Drawing and graphics

- Create fully customizable, high-performance graphics by drawing with Metal shaders inside a SwiftUI app using a [`Shader`](../SwiftUI/shader.md) structure.
- Configure an image with a specific dynamic range by applying the [`allowedDynamicRange(_:)`](../SwiftUI/view/alloweddynamicrange%28_%29.md) view modifier.
- Compose effects that you apply to a view based on some aspect of the geometry of the view using the [`visualEffect(_:)`](../SwiftUI/view/visualeffect%28_%29.md) modifier. For example, you can apply a blur that varies depending on the view’s position in the display.

### Layout

- Define custom coordinate spaces using the [`CoordinateSpaceProtocol`](../SwiftUI/coordinatespaceprotocol.md) with new [`GeometryProxy`](../SwiftUI/geometryproxy.md) methods, like [`bounds(of:)`](../SwiftUI/geometryproxy/bounds%28of%29.md) and [`frame(in:)`](../SwiftUI/geometryproxy/frame%28in%29-68tks.md), to get the dimensions of containers.
- Create a frame for a view that lays out its content based on characteristics of the container view using [`containerRelativeFrame(_:alignment:)`](../SwiftUI/view/containerrelativeframe%28_,alignment%29.md).
- Set the background of a container view using the [`containerBackground(_:for:)`](../SwiftUI/view/containerbackground%28_,for%29.md) view modifier.

### Lists and tables

- Disable selectability of an item in a [`List`](../SwiftUI/list.md) or [`Table`](../SwiftUI/table.md) by applying the [`selectionDisabled(_:)`](../SwiftUI/view/selectiondisabled%28_%29.md) modifier.
- Collapse or expand a [`Section`](../SwiftUI/section.md) of a list or table using the `isExpanded` binding in the section’s initializer.
- Configure row or section spacing using the [`listRowSpacing(_:)`](../SwiftUI/view/listrowspacing%28_%29.md) and [`listSectionSpacing(_:)`](../SwiftUI/view/listsectionspacing%28_%29-5t518.md) modifiers, respectively.
- Set the prominence of a badge using the [`badgeProminence(_:)`](../SwiftUI/view/badgeprominence%28_%29.md) view modifier.
- Configure alternating row backgrounds using the [`alternatingRowBackgrounds(_:)`](../SwiftUI/view/alternatingrowbackgrounds%28_%29.md) modifier.
- Customize table column visibility and reordering using the [`TableColumnCustomization`](../SwiftUI/tablecolumncustomization.md) structure.
- Add hierarchical rows to a table using the [`DisclosureTableRow`](../SwiftUI/disclosuretablerow.md) structure, or recursively hierarchical rows using the [`OutlineGroup`](../SwiftUI/outlinegroup.md) structure.
- Hide table column headers using the [`tableColumnHeaders(_:)`](../SwiftUI/view/tablecolumnheaders%28_%29.md) modifier.

### Scrolling

- Read the position of a scroll view using one of the scroll position modifiers, like [`scrollPosition(id:anchor:)`](../SwiftUI/view/scrollposition%28id,anchor%29.md).
- Flash scroll indicators programmatically using a view modifier, like [`scrollIndicatorsFlash(onAppear:)`](../SwiftUI/view/scrollindicatorsflash%28onappear%29.md).
- Clip scroll views in custom ways after disabling default clipping using the [`scrollClipDisabled(_:)`](../SwiftUI/view/scrollclipdisabled%28_%29.md) modifier.
- Create paged scroll views, aligned to either page or view boundaries, using the [`scrollTargetBehavior(_:)`](../SwiftUI/view/scrolltargetbehavior%28_%29.md) view modifier.
- Create custom scroll behaviors using the [`ScrollTargetBehavior`](../SwiftUI/scrolltargetbehavior.md) protocol.
- Control the insets of scrollable views using the [`safeAreaPadding(_:)`](../SwiftUI/view/safeareapadding%28_%29-5lh9p.md) and [`contentMargins(_:_:for:)`](../SwiftUI/view/contentmargins%28_,_,for%29-1lt8b.md) view modifiers.
- Add effects to views as they scroll on- and offscreen using one of the [`scrollTransition(_:axis:transition:)`](../SwiftUI/view/scrolltransition%28_,axis,transition%29.md) modifiers.
- Create a [`TabView`](../SwiftUI/tabview.md) that supports vertical paging in watchOS by applying the [`verticalPage`](../SwiftUI/tabviewstyle/verticalpage.md) tab view style.

### Gestures

- Make smoother transitions between gestures and animations by using a new [`velocity`](../SwiftUI/draggesture/value/velocity.md) property on the values associated with certain gestures and a [`tracksVelocity`](../SwiftUI/transaction/tracksvelocity.md) property on [`Transaction`](../SwiftUI/transaction.md).
- Gain access to more information, including both velocity and position, by migrating to the new [`MagnifyGesture`](../SwiftUI/magnifygesture.md) and [`RotateGesture`](../SwiftUI/rotategesture.md), which replace the now deprecated `MagnificationGesture` and `RotationGesture`.

### Input events

- Enable a view that’s in focus to react directly to keyboard input by applying one of the [`onKeyPress(_:action:)`](../SwiftUI/view/onkeypress%28_,action%29.md) view modifiers.
- Enable people to choose from a compact collection of items in a [`Menu`](../SwiftUI/menu.md) by styling a [`Picker`](../SwiftUI/picker.md) with the [`palette`](../SwiftUI/pickerstyle/palette.md) style.
- Provide haptic or audio feedback in response to an event using one of the sensory feedback modifiers, like [`sensoryFeedback(_:trigger:)`](../SwiftUI/view/sensoryfeedback%28_,trigger%29.md).
- Create buttons and toggles that perform an [`AppIntent`](../AppIntents/appintent.md) in a widget, Live Activity, and other places using new initializers like [`init(_:intent:)`](../SwiftUI/button/init%28_,intent%29-7urde.md) and [`init(_:isOn:intent:)`](../SwiftUI/toggle/init%28_,ison,intent%29-4lsrf.md).

### Focus

- Distinguish between views for which focus serves different purposes, such as those that have a primary action like a button and those that take input like a text field, using the new [`focusable(_:interactions:)`](../SwiftUI/view/focusable%28_,interactions%29.md) view modifier.
- Manage the effect that receiving focus has on a view using the [`focusEffectDisabled(_:)`](../SwiftUI/view/focuseffectdisabled%28_%29.md) modifier.

### Previews in Xcode

- Reduce the amount of boilerplate that you need to create Xcode previews by using the new [`Preview(_:traits:_:body:)`](../SwiftUI/preview%28_,traits,_,body%29.md) macro.

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

*[View on Apple Developer](https://developer.apple.com/documentation/updates/swiftui)*