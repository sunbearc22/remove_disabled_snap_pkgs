# remove_disabled_snap_pkgs

## Purpose: 
This python script automates the removal of all disabled SNAP packages. In so doing, it will violate SNAP's inherent redundancy capability to allow automated rollback when a SNAP application crashes or when its upgrade is corrupted. However, it can help free up a significant amount of disk space (e.g. ~30% of total disk space of all SNAP packages).   

## How to use the script? 
 1. Open a terminal and execute the python script as shown below. It will list all SNAP packages that are in the system, showing their "status", "bytes", "path". Those packages that are without the "Active" label are disabled, i.e. redundancy packages to allow automated rollbacks. The script will also list the total size of all the SNAP packages, and only "Active" and only "Disabled' packages.
 2. If disabled SNAP package(s) exist, you have to reply 'y' or 'n' to the question, "REMOVE ALL DISABLED SNAP PACKAGES?".

## Example
    $ python3 remove_disabled_snap_pkgs.py
    ALL (ACTIVE & DISABLED) SNAP PACKAGES IN SYSTEM:
    Active	    31899648	/var/lib/snapd/snaps/2048x_3.snap
    Active	   298893312	/var/lib/snapd/snaps/atom_282.snap
    Active	        4096	/var/lib/snapd/snaps/bare_5.snap
                75415552	/var/lib/snapd/snaps/bitwarden_58.snap
    Active	    75431936	/var/lib/snapd/snaps/bitwarden_59.snap
               205479936	/var/lib/snapd/snaps/blender_1113.snap
    Active	   223838208	/var/lib/snapd/snaps/blender_1237.snap
                 9461760	/var/lib/snapd/snaps/canonical-livepatch_119.snap
    Active	     9465856	/var/lib/snapd/snaps/canonical-livepatch_126.snap
                16990208	/var/lib/snapd/snaps/chromium-ffmpeg_23.snap
    Active	    18845696	/var/lib/snapd/snaps/chromium-ffmpeg_24.snap
               155017216	/var/lib/snapd/snaps/chromium_1854.snap
    Active	   154738688	/var/lib/snapd/snaps/chromium_1864.snap
                58191872	/var/lib/snapd/snaps/core18_2246.snap
    Active	    58183680	/var/lib/snapd/snaps/core18_2253.snap
                64835584	/var/lib/snapd/snaps/core20_1242.snap
    Active	    64913408	/var/lib/snapd/snaps/core20_1270.snap
               104271872	/var/lib/snapd/snaps/core_11798.snap
    Active	   104267776	/var/lib/snapd/snaps/core_11993.snap
               316801024	/var/lib/snapd/snaps/cura-slicer_57.snap
    Active	   316801024	/var/lib/snapd/snaps/cura-slicer_58.snap
                86917120	/var/lib/snapd/snaps/discord_130.snap
    Active	    86917120	/var/lib/snapd/snaps/discord_131.snap
               323358720	/var/lib/snapd/snaps/djpdf_58.snap
    Active	   353034240	/var/lib/snapd/snaps/djpdf_59.snap
    Active	    83968000	/var/lib/snapd/snaps/ffmpeg_1286.snap
    Active	   654024704	/var/lib/snapd/snaps/freecad_22.snap
               290496512	/var/lib/snapd/snaps/gimp_380.snap
    Active	   410279936	/var/lib/snapd/snaps/gimp_383.snap
    Active	   172761088	/var/lib/snapd/snaps/gnome-3-28-1804_161.snap
               229638144	/var/lib/snapd/snaps/gnome-3-34-1804_72.snap
    Active	   229638144	/var/lib/snapd/snaps/gnome-3-34-1804_77.snap
               254115840	/var/lib/snapd/snaps/gnome-3-38-2004_76.snap
    Active	   259948544	/var/lib/snapd/snaps/gnome-3-38-2004_87.snap
                68259840	/var/lib/snapd/snaps/gtk-common-themes_1515.snap
    Active	    68378624	/var/lib/snapd/snaps/gtk-common-themes_1519.snap
    Active	      143360	/var/lib/snapd/snaps/gtk2-common-themes_13.snap
               193802240	/var/lib/snapd/snaps/inkscape_9090.snap
    Active	   192770048	/var/lib/snapd/snaps/inkscape_9256.snap
                11747328	/var/lib/snapd/snaps/kapman_52.snap
    Active	     4059136	/var/lib/snapd/snaps/kapman_57.snap
    Active	   273375232	/var/lib/snapd/snaps/kde-frameworks-5-core18_32.snap
    Active	   185520128	/var/lib/snapd/snaps/krita_64.snap
    Active	    68575232	/var/lib/snapd/snaps/meshlab_183.snap
    Active	    57458688	/var/lib/snapd/snaps/mrrescue_117.snap
    Active	    40771584	/var/lib/snapd/snaps/ohmygiraffe_7.snap
               431214592	/var/lib/snapd/snaps/onlyoffice-desktopeditors_81.snap
    Active	   660430848	/var/lib/snapd/snaps/onlyoffice-desktopeditors_94.snap
    Active	    46014464	/var/lib/snapd/snaps/pin-town_2.snap
    Active	    65556480	/var/lib/snapd/snaps/reversit_2.snap
               236208128	/var/lib/snapd/snaps/riseup-vpn_172.snap
    Active	   241647616	/var/lib/snapd/snaps/riseup-vpn_179.snap
    Active	   116445184	/var/lib/snapd/snaps/simplenote_544.snap
               140914688	/var/lib/snapd/snaps/skype_194.snap
    Active	   140963840	/var/lib/snapd/snaps/skype_197.snap
                53432320	/var/lib/snapd/snaps/snap-store_547.snap
    Active	    56872960	/var/lib/snapd/snaps/snap-store_558.snap
                44220416	/var/lib/snapd/snaps/snapd_14066.snap
    Active	    45371392	/var/lib/snapd/snaps/snapd_14295.snap
               169922560	/var/lib/snapd/snaps/spotify_53.snap
    Active	   175443968	/var/lib/snapd/snaps/spotify_56.snap
    Active	   228057088	/var/lib/snapd/snaps/supertux_229.snap
    Active	   649035776	/var/lib/snapd/snaps/supertuxkart_639.snap
    Active	   310079488	/var/lib/snapd/snaps/vlc_2344.snap
    Active	   989949952	/var/lib/snapd/snaps/xonotic_64.snap
    Active	    97476608	/var/lib/snapd/snaps/youtube-dl_4572.snap
    Active	    65949696	/var/lib/snapd/snaps/zenkit_17.snap

    SIZE OF SNAP PACKAGES:
    1. All      :  11928915968 bytes
    2. Active   :   8388202496 bytes
    2. Disabled :   3540713472 bytes or 29.68% of All

    REMOVE ALL DISABLED SNAP PACKAGES? [y/n]
    y
    Removal in progress... pls wait

    sudo snap remove bitwarden --revision=58
    bitwarden (revision 58) removed

    sudo snap remove blender --revision=1113
    blender (revision 1113) removed

    sudo snap remove canonical-livepatch --revision=119
    canonical-livepatch (revision 119) removed

    sudo snap remove chromium-ffmpeg --revision=23
    chromium-ffmpeg (revision 23) removed

    sudo snap remove chromium --revision=1854
    chromium (revision 1854) removed

    sudo snap remove core18 --revision=2246
    core18 (revision 2246) removed

    sudo snap remove core20 --revision=1242
    core20 (revision 1242) removed

    sudo snap remove core --revision=11798
    core (revision 11798) removed

    sudo snap remove cura-slicer --revision=57
    cura-slicer (revision 57) removed

    sudo snap remove discord --revision=130
    discord (revision 130) removed

    sudo snap remove djpdf --revision=58
    djpdf (revision 58) removed

    sudo snap remove gimp --revision=380
    gimp (revision 380) removed

    sudo snap remove gnome-3-34-1804 --revision=72
    gnome-3-34-1804 (revision 72) removed

    sudo snap remove gnome-3-38-2004 --revision=76
    gnome-3-38-2004 (revision 76) removed

    sudo snap remove gtk-common-themes --revision=1515
    gtk-common-themes (revision 1515) removed

    sudo snap remove inkscape --revision=9090
    inkscape (revision 9090) removed

    sudo snap remove kapman --revision=52
    kapman (revision 52) removed

    sudo snap remove onlyoffice-desktopeditors --revision=81
    onlyoffice-desktopeditors (revision 81) removed

    sudo snap remove riseup-vpn --revision=172
    riseup-vpn (revision 172) removed

    sudo snap remove skype --revision=194
    skype (revision 194) removed

    sudo snap remove snap-store --revision=547
    snap-store (revision 547) removed

    sudo snap remove snapd --revision=14066
    snapd (revision 14066) removed

    sudo snap remove spotify --revision=53
    spotify (revision 53) removed
    
    REMOVE ALL DISABLED SNAP PACKAGES? COMPLETED.
