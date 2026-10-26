# Gestalt Manager

**Framework**: Core Services  
**Role**: API Collection

Investigate the operating environment of your app.

> **Deprecated**: In macOS 10.8 and later, use [`ProcessInfo`](../../Foundation/processinfo.md) or `sysctl` instead.

## Topics

### Result Codes
- [var gestaltUnknownErr: Int](../gestaltunknownerr.md)
  Specifies an unknown error.
- [var gestaltUndefSelectorErr: Int](../gestaltundefselectorerr.md)
  Specifies an undefined selector was passed to the Gestalt Manager.
- [var gestaltDupSelectorErr: Int](../gestaltdupselectorerr.md)
  Specifies you tried to add an entry that already existed.
- [var gestaltLocationErr: Int](../gestaltlocationerr.md)
  Specifies the gestalt function ptr was not in the system heap.
- [gestaltUnknownErr](../api-1559958-anonymous/gestaltunknownerr.md)
  Specifies an unknown error.
- [gestaltUndefSelectorErr](../api-1559958-anonymous/gestaltundefselectorerr.md)
  Specifies an undefined selector was passed to the Gestalt Manager.
- [gestaltDupSelectorErr](../api-1559958-anonymous/gestaltdupselectorerr.md)
  Specifies you tried to add an entry that already existed.
- [gestaltLocationErr](../api-1559958-anonymous/gestaltlocationerr.md)
  Specifies the gestalt function ptr was not in the system heap.
### Getting and Setting Gestalt Selector Codes and Values
- [Gestalt](../api-1471624-gestalt.md)
  Obtains information about the operating environment.
- [NewGestaltValue](../api-1472055-newgestaltvalue.md)
  Installs a new `Gestalt` selector code and a value that `Gestalt` returns for that selector.
- [SetGestaltValue](../api-1470991-setgestaltvalue.md)
  Sets the value the function `Gestalt` will return for a specified selector code, installing the selector if it was not already installed.
- [ReplaceGestaltValue](../api-1472000-replacegestaltvalue.md)
  Replaces the value that the function `Gestalt` returns for a specified selector code with the value provided to the function.
- [DeleteGestaltValue](../api-1472699-deletegestaltvalue.md)
  Deletes a `Gestalt` selector code so that it is no longer recognized by `Gestalt`.
### Working With Universal Procedure Pointers for Gestalt Selector Functions
- [NewSelectorFunctionUPP](../api-1472304-newselectorfunctionupp.md)
  Creates a universal procedure pointer (UPP) to a selector callback function.
- [DisposeSelectorFunctionUPP](../api-1472149-disposeselectorfunctionupp.md)
  Disposes of a universal procedure pointer to a selector callback function.
- [InvokeSelectorFunctionUPP](../api-1473043-invokeselectorfunctionupp.md)
  Invokes a selector callback function.
### Callbacks
- [SelectorFunctionProcPtr](../selectorfunctionprocptr.md)
  Defines a pointer to a selector callback function that returns information associated with your own selector code.  
### Data Types
- [SelectorFunctionUPP](../selectorfunctionupp.md)
  Defines a universal procedure pointer to a selector function callback.
### Constants
- [Addressing Mode Attribute Selectors](../api-1473033-addressing_mode_attribute_select.md)
  Specify feature availability information for the addressing mode of the operating system.
- [Admin Attribute Selectors](../api-1472053-admin_attribute_selectors.md)
  Specify feature availability for Macintosh Manager administration software. 
- [AFP Client Selectors](../api-1471420-afp_client_selectors.md)
  Specify version and feature availability information for the AFP client.
- [Alias Manager Attribute Selectors](../api-1472727-alias_manager_attribute_selector.md)
  Specify feature availability information for the Alias Manager.
- [Appearance Manager Attribute Selectors](../api-1472012-appearance_manager_attribute_sel.md)
  Specify feature availability information for the Appearance Manager.
- [Appearance Manager Version Selector](../api-1471531-appearance_manager_version_selec.md)
  Specifies version information for the Appearance Manager.
- [Apple Event Manager Attribute Selectors](../api-1472598-apple_event_manager_attribute_se.md)
  Specify feature availability information for the Apple Event Manager.
- [AppleScript Attribute Selectors](../api-1472032-applescript_attribute_selectors.md)
  Specify feature availability information for AppleScript.
- [AppleScript Version Selector](../api-1471008-applescript_version_selector.md)
  Specifies version information for AppleScript.
- [AppleTalk Driver Version Selector](../api-1471416-appletalk_driver_version_selecto.md)
  Specifies version information for the AppleTalk driver.
- [AppleTalk Version Selector](../api-1472127-appletalk_version_selector.md)
  Specifies version information for AppleTalk.
- [ATSUI Attribute Selectors](../api-1471588-atsui_attribute_selectors.md)
  Specify feature availability for Apple Type Services for Unicode Imaging.
- [ATSUI Version Selectors](../api-1472731-atsui_version_selectors.md)
  Specify version information for Apple Type Service for Unicode Imaging.
- [ATA Manager Attribute Selectors](../api-1472485-ata_manager_attribute_selectors.md)
  Specify feature availability information for the ATA Manager.
- [AUX Version Selector](../api-1471353-aux_version_selector.md)
  Specifies version information for A/UX.
- [AVL Tree Attribute Selectors](../api-1472193-avl_tree_attribute_selectors.md)
  Specify feature availability information for AVL tree routines.
- [Bus Clock Version Selector](../api-1471795-bus_clock_version_selector.md)
  Specifies version information for the bus clock speed.
- [Carbon Version Selector](../api-1472844-carbon_version_selector.md)
  Specifies version information for Carbon.
- [Classic Compatibility Attribute Selectors](../api-1472089-classic_compatibility_attribute_.md)
  Specify feature availability for the Classic environment.
- [CloseView Attribute Selectors](../api-1472410-closeview_attribute_selectors.md)
  Specify feature availability information for CloseView.
- [Code Fragment Manager Attribute Selectors](../api-1471030-code_fragment_manager_attribute_.md)
  Specify feature availability information for the Code Fragment Manager.
- [Collection Manager Version Selector](../api-1471484-collection_manager_version_selec.md)
  Specify version information for the Collection manager.
- [Color Picker Version Selectors](../api-1470900-color_picker_version_selectors.md)
  Specify version information for the Color Picker.
- [ColorSync Manager Attribute Selectors](../api-1473015-colorsync_manager_attribute_sele.md)
  Specify feature availability information for the ColorSync Manager.
- [ColorSync Manager Version Selectors](../api-1472872-colorsync_manager_version_select.md)
  Specify version information for the ColorSync Manager.
- [Communications Toolbox Version Selector](../api-1472785-communications_toolbox_version_s.md)
  Specifies version information for the Communications Toolbox.
- [Communication Resource Manager Attribute Selectors](../api-1471045-communication_resource_manager_a.md)
  Specify version and feature availability information for the Communications Resource Manager.
- [Component Manager Version Selectors](../api-1472789-component_manager_version_select.md)
  Specify version information for the Component Manager.
- [Computer Model Selectors](../api-1473025-computer_model_selectors.md)
  Specify computer models.
- [Computer Name Selector](../api-1471661-computer_name_selector.md)
  Specifies user-visibility information for the computer name.
- [Connection Manager Attribute Selectors](../api-1472521-connection_manager_attribute_sel.md)
  Specify feature availability information for the Connection Manager.
- [Control Manager Attribute Selectors](../api-1472620-control_manager_attribute_select.md)
  Specify feature availability information for the Control Manager.
- [Control Manager Version Selector](../api-1471614-control_manager_version_selector.md)
  Specifies version information for the Control Manager.
- [Control Strip Attribute Selectors](../api-1471121-control_strip_attribute_selector.md)
  Specify feature availability for the Control Strip.
- [Control Strip Version Selector](../api-1471496-control_strip_version_selector.md)
  Specifies version information for the Control Strip.
- [CPU Selectors for Apollo](../api-1471879-cpu_selectors_for_apollo.md)
  Specify version information for Apollo CPUs.
- [CPU Selectors for Intel and Pentium](../api-1473138-cpu_selectors_for_intel_and_pent.md)
  Specify version information for Intel and Pentium CPUs.
- [Data Access Manager Attribute Selectors](../api-1472559-data_access_manager_attribute_se.md)
  Specify feature availability information for the Data Access Manager.
- [Desktop Pictures Attribute Selectors](../api-1471883-desktop_pictures_attribute_selec.md)
  Specify feature availability information for Desktop Pictures.
- [Desktop Printing Attribute Selector](../api-1471871-desktop_printing_attribute_selec.md)
  Specify feature availability information for all desktop printer.
- [Desktop Printing Driver Attribute Selectors](../api-1471074-desktop_printing_driver_attribut.md)
  Specify feature availability for third-party desktop printing drivers.
- [Dialog Manager Attribute Selectors](../api-1470790-dialog_manager_attribute_selecto.md)
  Specify feature availability for the Dialog Manager.
- [Dictionary Manager Attribute Selectors](../api-1472002-dictionary_manager_attribute_sel.md)
  Specify feature availability information for the Dictionary Manager.
- [Dialog Manager Selectors for Mac OS 8.5](../api-1473152-5.md)
  Specify version and feature availability information for the Dialog Manager in Mac OS 8.5.
- [Digital Signature Version Selector](../api-1472022-digital_signature_version_select.md)
  Specifies version information for digital signatures.
- [Direct IO Attribute Selector](../api-1471893-direct_io_attribute_selector.md)
  Specifies availability of direct input/output support by the file system.
- [Disk Cache Size Selector](../api-1471577-disk_cache_size_selector.md)
  Specifies size information for the disk cache buffer.
- [Display Manager Attribute Selectors](../api-1471733-display_manager_attribute_select.md)
  Specify feature availability for the Display Manager.
- [Display Manager Version Selector](../api-1472759-display_manager_version_selector.md)
  Specifies version information for the Display Manager.
- [Drag Manager Attribute Selectors](../api-1472964-drag_manager_attribute_selectors.md)
  Specify feature availability information for the Drag Manager.
- [Draw Sprocket Version Selectors](../api-1471909-draw_sprocket_version_selectors.md)
  Specifies version information for Draw Sprocket.
- [Easy Access Selectors](../api-1470871-easy_access_selectors.md)
  Specify version and feature availability information for Easy Access.
- [Edition Manager Attribute Selectors](../api-1472799-edition_manager_attribute_select.md)
  Specify feature availability for the Edition Manager.
- [Extension Table Version Selector](../api-1470995-extension_table_version_selector.md)
  Specifies version information for the extension table.
- [File Mapping Attribute Selectors](../api-1470869-file_mapping_attribute_selectors.md)
  Specify feature availability for file mapping.
- [File System Attribute Selectors](../api-1471227-file_system_attribute_selectors.md)
  Specify feature availability for the file system.
- [File System Attribute Selectors for Mac OS 9](../api-1471735-file_system_attribute_selectors_.md)
  Specify feature availability for the file system for features introduced in Mac OS 9.
- [File System Manager Version Selector](../api-1470924-file_system_manager_version_sele.md)
  Specifies version information for the File System Manager.
- [File System Transport Manager Attribute Selectors](../api-1471756-file_system_transport_manager_at.md)
  Specify feature availability for the File System Transport Manager
- [Find By Content State Selectors](../api-1472020-find_by_content_state_selectors.md)
  Specify state information for Find By Content.
- [Find By Content Version Selectors](../api-1471442-find_by_content_version_selector.md)
  Specify version information for Find By Content.
- [Find Folder Redirection Attribute Selector](../api-1471215-find_folder_redirection_attribut.md)
  Specifies feature availability information for Find Folder.
- [Finder Attribute Selectors](../api-1473027-finder_attribute_selectors.md)
  Specify feature availability for the Finder.
- [Floppy Driver Attribute Selectors](../api-1472773-floppy_driver_attribute_selector.md)
  Specify feature availability information for the floppy disk drive.
- [Font Manager Attribute Selectors](../api-1472955-font_manager_attribute_selectors.md)
  Specify feature availability information for the Font Manager.
- [Folder Manager Attribute Selectors](../api-1473089-folder_manager_attribute_selecto.md)
  Specify feature availability information for the Folder Manager.
- [FPU Type Selectors](../api-1471986-fpu_type_selectors.md)
  Specify version and availability information for the type of floating-point unit installed.
- [Gestalt Manager Version Selectors](../api-1471247-gestalt_manager_version_selector.md)
  Specify Gestalt Manager version information. 
- [Hardware Attribute Attribute Selectors](../api-1472318-hardware_attribute_attribute_sel.md)
  Specify feature availability information for hardware.
- [Hardware Icon Selector](../api-1470875-hardware_icon_selector.md)
  Specifies icon family resource ID information for the computer hardware.
- [Hardware Vendor Selectors](../api-1472248-hardware_vendor_selectors.md)
  Specify hardware vendor information.
- [Help Manager Attribute Selectors](../api-1472846-help_manager_attribute_selectors.md)
  Specify feature availability for the Apple Help Manager.
- [Icon Services Attribute Selectors](../api-1471107-icon_services_attribute_selector.md)
  Specify feature availability for Icon Services.
- [Image Compression Manager Version Selector](../api-1471141-image_compression_manager_versio.md)
  Specifies the version of the Image Compression Manager.
- [Internal Display Location Selector](../api-1472200-internal_display_location_select.md)
  Specifies the slot number information for the internal display location.
- [Keyboard Selectors](../api-1471510-keyboard_selectors.md)
  Specify keyboard information.
- [Keyboard Selectors for Laptops](../api-1473172-keyboard_selectors_for_laptops.md)
  Specify laptop keyboard information.
- [Logical Page Size Selector](../api-1471519-logical_page_size_selector.md)
  Specifies logical page size information.
- [Logical RAM Size Selector](../api-1472097-logical_ram_size_selector.md)
  Specifies logical random-access memory size information.
- [Low Memory Size Selector](../api-1471061-low_memory_size_selector.md)
  Specifies information about the size of the low-memory area.
- [Machine Name String ID](../api-1472878-machine_name_string_id.md)
  Defines a machine name string ID.
- [Mailer Version Selector](../api-1473176-mailer_version_selector.md)
  Specifies version information for the OCE standard mailer.
- [Mailer Send LetterVersion Selector](../api-1470987-mailer_send_letterversion_select.md)
  Specifies version information for the OCE standard mailer’s send letter.
- [Media Bay Selectors](../api-1472073-media_bay_selectors.md)
  Specify information about media bay availability.
- [Memory Attribute Selectors](../api-1471646-memory_attribute_selectors.md)
  Specify feature availability information for memory.
- [Memory Mapping Attribute Selectors](../api-1472928-memory_mapping_attribute_selecto.md)
  Specify feature availability information for memory mapping.
- [Menu Manager Selectors in Mac OS 8.5](../api-1472592-5.md)
  Specify version and feature availability information for the Menu Manager in Mac OS 8.5
- [Message Manager Version Selector](../api-1472970-message_manager_version_selector.md)
  Specify version information for the Message Manager.
- [Miscellaneous Attribute Selectors](../api-1472984-miscellaneous_attribute_selector.md)
  Specify feature availability information for miscellaneous pieces of the operating system or the hardware configuration.
- [Mixed Mode Manager Selectors](../api-1472719-mixed_mode_manager_selectors.md)
  Specify version and feature availability information for the Mixed Mode Manager.
- [Mixed Mode Manager Version Selector](../api-1471159-mixed_mode_manager_version_selec.md)
  Specifies version information for the Mixed Mode Manager.
- [MMU Type Selectors](../api-1472336-mmu_type_selectors.md)
  Specify information about the type of MMU installed.
- [Multiple Users State Selector](../api-1472662-multiple_users_state_selector.md)
  Specifies information about the multiple user state.
- [Name-Binding Protocol Attribute Selectors](../api-1472826-name-binding_protocol_attribute_selec.md)
  Specify feature availability information for the standard name-binding protocol.
- [Name Registry Version Selector](../api-1472514-name_registry_version_selector.md)
  Specifies the version of the name registry.
- [Native CPU Selectors](../api-1471500-native_cpu_selectors.md)
  Specify the native CPU type or family.
- [Notification Manager Attribute Selectors](../api-1471014-notification_manager_attribute_s.md)
  Specify feature availability information for the Notification Manager.
- [NuBus Location Selector](../api-1471694-nubus_location_selector.md)
  Specifies information about the NuBus slot connector locations.
- [NuBus Slot Count Selector](../api-1472452-nubus_slot_count_selector.md)
  Specifies information about the number of NuBus slots.
- [OCE Toolbox Attribute Selectors](../api-1470848-oce_toolbox_attribute_selectors.md)
  Specify feature availability for the OCE Toolbox.
- [OCE Toolbox Version Selectors](../api-1471959-oce_toolbox_version_selectors.md)
  Specify version information for the OCE Toolbox.
- [Open Firmware Selector](../api-1471858-open_firmware_selector.md)
  Specifies version information for Open Firmware.
- [Open Firmware Safe Selectors](../api-1472041-open_firmware_safe_selectors.md)
  Specify feature availability for Open Firmware safe features. 
- [Open Transport Selectors](../api-1471584-open_transport_selectors.md)
  Specify version and feature availability information for Open Transport.
- [Open Transport Network Setup Selectors](../api-1471729-open_transport_network_setup_sel.md)
  Specify feature availability and setup information for Open Transport networking.
- [Open Transport Network Version Selector](../api-1471360-open_transport_network_version_s.md)
  Specifies the version of the Open Transport network setup.
- [Open Transport Remote Access Selectors](../api-1471891-open_transport_remote_access_sel.md)
  Specify feature availability for Open Transport remote access.
- [Opent Transport Remote Access Version Selector](../api-1472078-opent_transport_remote_access_ve.md)
  Specifies version information for Open Transport remote access.
- [Open Transport Version Selector](../api-1471885-open_transport_version_selector.md)
  Specifies version information for Open Transport.
- [OS Trap Table Selector](../api-1471320-os_trap_table_selector.md)
  Specifies base address information for the operating system trap dispatch table.
- [Parity Checking Attribute Selectors](../api-1470865-parity_checking_attribute_select.md)
  Specify feature availability for parity checking.
- [PC Compatibility Card Selectors](../api-1472039-pc_compatibility_card_selectors.md)
  Specify version and feature availability information for a PC-compatibility card.
- [PC Exchange Attribute Selectors](../api-1472585-pc_exchange_attribute_selectors.md)
  Specify feature availability information for PC Exchange.
- [Physical RAM Size Selector](../api-1472400-physical_ram_size_selector.md)
  Specifies information about the size of the physical RAM.
- [Pop-up Control Selector](../api-1472648-pop-up_control_selector.md)
  Specify feature availability for pop-up controls.
- [Power Manager Attribute Selectors](../api-1472525-power_manager_attribute_selector.md)
  Specify feature availability for the Power Manager.
- [Power Manager Version Selector](../api-1471630-power_manager_version_selector.md)
  Specifies version information for the Power Manager.
- [PowerPC Attribute Selectors](../api-1472037-powerpc_attribute_selectors.md)
  Specify feature availability for PowerPC processors.
- [PowerPC Toolbox Attribute Selectors](../api-1471990-powerpc_toolbox_attribute_select.md)
  Specify feature availability for the PowerPC Toolbox.
- [Preemptive Function Attribute Selectors](../api-1472095-preemptive_function_attribute_se.md)
  Specify feature availability information for preemptive system software functions.
- [Processor Clock Speed Selector](../api-1472292-processor_clock_speed_selector.md)
  Specifies information about processor clock speed.
- [Processor Type Selector](../api-1471022-processor_type_selector.md)
  Specifies information about the type of microprocessor.
- [Quadra Redefinitions](../api-1470744-quadra_redefinitions.md)
  Specifies alternate names for MacQuadra constants.
- [QuickDraw 3D Attribute Selectors](../api-1472491-quickdraw_3d_attribute_selectors.md)
  Specify feature availability information for QuickDraw 3D.
- [Quick Draw 3D Version Selector](../api-1471083-quick_draw_3d_version_selector.md)
  Specifies version information for QuickDraw 3D.
- [QuickDraw 3D Viewer Attribute Selectors](../api-1471854-quickdraw_3d_viewer_attribute_se.md)
  Specify feature availability information for QuickDraw 3D Viewer.
- [QuickDraw Attribute Selectors](../api-1471772-quickdraw_attribute_selectors.md)
  Specify feature availability information for QuickDraw.
- [QuickDraw Version Selectors](../api-1472475-quickdraw_version_selectors.md)
  Specify version information for QuickDraw.
- [QuickDraw GX Overall Version Selector](../api-1472227-quickdraw_gx_overall_version_sel.md)
  Specifies version information for the overall version of QuickDraw GX.
- [QuickDraw GX Printing Version Selector](../api-1472932-quickdraw_gx_printing_version_se.md)
  Specifies version information for QuickDraw GX printing.
- [QuickDraw GX Version Selectors](../api-1472848-quickdraw_gx_version_selectors.md)
  Specify version information for QuickDraw GX.
- [QuickDraw GX Attribute Selectors](../api-1472953-quickdraw_gx_attribute_selectors.md)
  Specify feature availability information for QuickDraw GX.
- [QuickDraw Text Attribute Selectors](../api-1470985-quickdraw_text_attribute_selecto.md)
  Specify feature availability information for QuickDraw Text.
- [QuickDraw Text Version Selectors](../api-1471465-quickdraw_text_version_selectors.md)
  Specify version information for QuickDraw Text.
- [QuickTime VR Feature Selectors](../api-1471865-quicktime_vr_feature_selectors.md)
  Specify feature availability information for QuickTime VR.
- [QuickTime VR Version Selector](../api-1472308-quicktime_vr_version_selector.md)
  Specifies version information for QuickTime VR.
- [QuickTime Attribute Selectors](../api-1472880-quicktime_attribute_selectors.md)
  Specify feature availability information for QuickTime.
- [QuickTime Version Selectors](../api-1471602-quicktime_version_selectors.md)
  Specify version information for QuickTime.
- [QuickTime Conferencing Information Selector](../api-1471315-quicktime_conferencing_informati.md)
  Specifies information about QuickTime conferencing.
- [QuickTime Conferencing Selector](../api-1470844-quicktime_conferencing_selector.md)
  Specifies availability information for QuickTime conferencing.
- [QuickTime Streaming Attribute Selector](../api-1471964-quicktime_streaming_attribute_se.md)
  Specify feature availability information for QuickTime streaming.
- [QuickTime Streaming Version Selector](../api-1472813-quicktime_streaming_version_sele.md)
  Specifies version information for QuickTime streaming.
- [RBV Address Selector](../api-1472214-rbv_address_selector.md)
  Specifies information about the RBV base address.
- [Realtime Manager Attribute Selectors](../api-1472656-realtime_manager_attribute_selec.md)
  Specify feature availability information for the Realtime Manager.
- [Resource Manager Bug Fixes Attribute Selectors](../api-1472014-resource_manager_bug_fixes_attri.md)
  Specify feature availability information for Resource Manager bug fixes.
- [Resource Manager Attribute Selectors](../api-1471343-resource_manager_attribute_selec.md)
  Specify feature availability information for the Resource Manager.
- [ROM Size Selector](../api-1472914-rom_size_selector.md)
  Specifies information about ROM size information.
- [ROM Version Selector](../api-1472244-rom_version_selector.md)
  Specifies ROM version information.
- [SCC Read Address Selector](../api-1472898-scc_read_address_selector.md)
  Specifies information about the base address for reading SCC.
- [SCC Write Address Selector](../api-1472660-scc_write_address_selector.md)
  Specifies information about the base address for writing SCC.
- [SCSI Manager Attribute Selectors](../api-1472992-scsi_manager_attribute_selectors.md)
  Specify feature availability information for the SCSI Manager.
- [Scrap Manager Selectors](../api-1471486-scrap_manager_selectors.md)
  Specify version and feature availability information for the Scrap Manager.
- [Screen Capture Selectors](../api-1472082-screen_capture_selectors.md)
  Specifies location information for screen capture.
- [Script Manager Version Selector](../api-1471836-script_manager_version_selector.md)
  Specifies version information for the Script Manager.
- [Script Systems Count Selector](../api-1471467-script_systems_count_selector.md)
  Specifies information about the number of active script systems.
- [Serial Hardware Attribute Selectors](../api-1471382-serial_hardware_attribute_select.md)
  Specify serial hardware attributes.
- [Serial Port Arbitrator Attribute Selectors](../api-1472884-serial_port_arbitrator_attribute.md)
  Specify feature availability information for serial port arbitration.
- [Settings Manager Attribute Selectors](../api-1471225-settings_manager_attribute_selec.md)
  Specify feature availability information for the Settings Manager.
- [Settings Manager Location Selector](../api-1471748-settings_manager_location_select.md)
  Specifies location information for the Settings Manager.
- [Settings Manager Version Selector](../api-1472513-settings_manager_version_selecto.md)
  Specifies version information for the Settings Manager.
- [Shutdown Attribute Selectors](../api-1472824-shutdown_attribute_selectors.md)
  Specify shutdown attributes.
- [Single Window Mode Selectors](../api-1471651-single_window_mode_selectors.md)
  Specify single-window modes.
- [Slot Attribute Selectors](../api-1471070-slot_attribute_selectors.md)
  Specify feature availability for slots.
- [Slot Number Selector](../api-1471977-slot_number_selector.md)
  Specifies information about the first physical slot in the computer.
- [Software Vendor Codes](../api-1470800-software_vendor_codes.md)
  Specify codes for software vendors.
- [Sound Manager Attribute Selectors](../api-1473081-sound_manager_attribute_selector.md)
  Specify feature availability information for the Sound Manager.
- [Speech Manager Attribute Selectors](../api-1472143-speech_manager_attribute_selecto.md)
  Specify feature availability information for the Speech Manager.
- [Speech Recognition Version Selector](../api-1472579-speech_recognition_version_selec.md)
  Specifies version information for the Speech Recognition Manager.
- [Speech Recognition Manager Attribute Selectors](../api-1471330-speech_recognition_manager_attri.md)
  Specify feature availability information for the Speech Recognition Manager.
- [Standard Directory Find Panel Selector](../api-1470760-standard_directory_find_panel_se.md)
  Specifies version information for the standard directory find panel.
- [Standard Directory Prompt Panel Selector](../api-1471177-standard_directory_prompt_panel_.md)
  Specifies version information for the standard directory prompt panel.
- [Standard Directory Version Selector](../api-1471370-standard_directory_version_selec.md)
  Specifies version information for the standard directory.
- [Startup Disk Attribute Selectors](../api-1471774-startup_disk_attribute_selectors.md)
  Specify feature availability information for the startup disk.
- [Standard File Attribute Selectors](../api-1471209-standard_file_attribute_selector.md)
  Specify feature availability information for Standard File.
- [System Architecture Selectors](../api-1472163-system_architecture_selectors.md)
  Specify the native system architecture.
- [System Update Version Selector](../api-1472561-system_update_version_selector.md)
  Indicates version information for system updates.
- [System Version Selectors](../api-1470788-system_version_selectors.md)
  Indicates operating system version information.
- [Telephone Manager Attribute Selectors](../api-1471396-telephone_manager_attribute_sele.md)
  Specify feature availability information for the Telephone Manager.
- [Terminal Manager Attribute Selectors](../api-1472262-terminal_manager_attribute_selec.md)
  Specify feature availability information for the Terminal Manager.
- [TextEdit Attribute Selectors](../api-1472145-textedit_attribute_selectors.md)
  Specify feature availability information for TextEdit.
- [TextEdit Version Selectors](../api-1472747-textedit_version_selectors.md)
  Specify version information for TextEdit.
- [Text Services Manager Attribute Selectors](../api-1472276-text_services_manager_attribute_.md)
  Specify feature availability information for the Text Services Manager.
- [Text Services Manager Version Selectors](../api-1471687-text_services_manager_version_se.md)
  Specifies version information for the Text Services Manager.
- [Thread Manager Attribute Selectors](../api-1472327-thread_manager_attribute_selecto.md)
  Specify feature availability information for the Thread Manager.
- [Time Manager Version Selectors](../api-1472047-time_manager_version_selectors.md)
  Specify version information for the Time Manager.
- [Toolbox Trap Table Selector](../api-1471440-toolbox_trap_table_selector.md)
  Specifies base address information for the Toolbox trap dispatch table.
- [Toolbox Trap Table (Second Half) Selector](../api-1471024-toolbox_trap_table_second_half_s.md)
  Specifies address information for the second half of the Toolbox trap table.
- [Translation Manager Attribute Selectors](../api-1471996-translation_manager_attribute_se.md)
  Specify feature availability information for the Translation Manager.
- [TSME Version Selector](../api-1472429-tsme_version_selector.md)
  Specifies version information for the Text Services Manager integrated with TextEdit.
- [TSMTE Attribute Selectors](../api-1471984-tsmte_attribute_selectors.md)
  Specify feature availability information for TSMTE.
- [TSMTE Version Selectors](../api-1472447-tsmte_version_selectors.md)
  Specify version information for TSMTE.
- [TV Tuner Attribute Selectors](../api-1470934-tv_tuner_attribute_selectors.md)
  Specifies feature availability information for the TV tuner.
- [UDF Selector](../api-1473049-udf_selector.md)
  Specifies support information for communication between implementations of UDF .
- [USB Attribute Selectors](../api-1471055-usb_attribute_selectors.md)
  Specifies feature availability information for USB.
- [USB Printer Sharing Version Selectors](../api-1470826-usb_printer_sharing_version_sele.md)
  Specify version information for USB printer sharing.
- [USB Version Selector](../api-1472690-usb_version_selector.md)
  Specifies version information for USB.
- [VIA1 Base Address Selector](../api-1473077-via1_base_address_selector.md)
  Specifies base address information for VIA 1.
- [VIA2 Base Address Selector](../api-1471692-via2_base_address_selector.md)
  Specifies base address information for VIA 2.
- [Virtual Memory Manager Attribute Selectors](../api-1471292-virtual_memory_manager_attribute.md)
  Specify feature availability information for the Virtual Memory Manager.
- [Virtual Memory Backing Store Selector](../api-1472936-virtual_memory_backing_store_sel.md)
  Specifies file reference number information for the VM backing store.
- [Virtual Memory Information Type Selectors](../api-1473148-virtual_memory_information_type_.md)
  Specifies information about the VM type.
- [Win32 Attribute Selectors](../api-1472139-win32_attribute_selectors.md)
  Specify feature availability information for Win32.
- [Window Manager Attribute Selectors](../api-1472830-window_manager_attribute_selecto.md)
  Specify feature availability information for the Window Manager.
- [WorldScriptII Version Selectors](../api-1470754-worldscriptii_version_selectors.md)
  Specify version information for WorldScript II.

## See Also

### Managers
- [Component Manager](./component_manager.md)
  Find and use components in your app or add custom components to system-provided services, such as QuickTime and Core Audio. 
- [Text Encoding Conversion Manager](./text_encoding_conversion_manager.md)
  Handle text encoding conversion between apps and transfer text across different platforms.
- [Alias Manager](./alias_manager.md)
  Create and resolve alias records that describe file system objects such as files, directories, and volumes. 
- [File Manager](./file_manager.md)
  Interact with files, folders, and volumes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/carbon_core/gestalt_manager)*