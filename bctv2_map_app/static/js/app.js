var map, featureList, pointSearch = [], tour;


    L.MakiMarkers.accessToken = "pk.eyJ1IjoiZ2VvbWFqb3I1NiIsImEiOiJjaW9iejZ4cGYwNDc0dnpsejBmc2g0Z3QzIn0.8hKDWYbdQW7cbIE7eeu4-A";

    $(document).ready(function () {

        console.log('Hey MotherFuckers!!!')

        $("#welcome").modal("show");
        $(window).resize(function () {
            sizeLayerControl();
        });

        $(document).on("click", ".feature-row", function (e) {
            $(document).off("mouseout", ".feature-row", clearHighlight);
            sidebarClick(parseInt($(this).attr("id"), 10));
        });

        if (!("ontouchstart" in window)) {
            $(document).on("mouseover", ".feature-row", function (e) {
                highlight.clearLayers().addLayer(L.circleMarker([$(this).attr("lat"), $(this).attr("lng")], highlightStyle));
            });
        }

        // $(document).on("mouseout", ".feature-row", clearHighlight);


        $("#legend-btn").click(function () {
            $("#legendModal").modal("show");
            $(".navbar-collapse.in").collapse("hide");
            return false;
        });

        $("#slideshow-btn").click(function () {
            jQuery("#bct_nanogallery2").nanogallery2({
                userID: '66767545@N02',
                kind: 'flickr',
                // displayBreadcrumb: 'false',
                thumbnailWidth: 150,
                thumbnailHeight: 150,
                colorScheme: 'dark',
                galleryDisplayMode: "pagination",
                galleryMaxRows: 2,
                galleryPaginationMode: "numbers",
                album: 'none',


            });
            $("#slideshowModal").modal("show");
            $(".navbar-collapse.in").collapse("hide");
            return false;
        });
    });
