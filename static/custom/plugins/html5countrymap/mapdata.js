const region_color = "#0B5B80"
const hover_color = "#fc9a06"


function openDetails(region) {
    console.log(region);
}


var simplemaps_countrymap_mapdata={
    main_settings: {
        // General settings
        width: "700", // '700' or 'responsive'
        background_color: "#FFFFFF",
        background_transparent: "yes",
        border_color: "#ffffff",
        state_description: "",
        state_color: "",
        state_hover_color: "",
        state_url: "",
        border_size: 1.5,
        all_states_inactive: "no",
        all_states_zoomable: "no",

        // Location defaults
        location_description: "Location description",
        location_url: "",
        location_color: "#FF0067",
        location_opacity: 0.8,
        location_hover_opacity: 1,
        location_size: 25,
        location_type: "square",
        location_image_source: "frog.png",
        location_border_color: "#FFFFFF",
        location_border: 2,
        location_hover_border: 2.5,
        all_locations_inactive: "no",
        all_locations_hidden: "no",

        // Label defaults
        label_color: "#d5ddec",
        label_hover_color: "#d5ddec",
        label_size: 22,
        label_font: "Arial",
        hide_labels: "no",
        hide_eastern_labels: "no",

        // Zoom settings
        zoom: "no",
        manual_zoom: "no",
        back_image: "no",
        initial_back: "no",
        initial_zoom: "-1",
        initial_zoom_solo: "no",
        region_opacity: 1,
        region_hover_opacity: 0.6,
        zoom_out_incrementally: "no",
        zoom_percentage: 0.99,
        zoom_time: 0.5,

        // Popup settings
        popup_color: "white",
        popup_opacity: 0.9,
        popup_shadow: 1,
        popup_corners: 5,
        popup_font: "12px/1.5 Verdana, Arial, Helvetica, sans-serif",
        popup_nocss: "no",

        // Advanced settings
        div: "map",
        auto_load: "yes",
        url_new_tab: "no",
        images_directory: "default",
        fade_time: 0.1,
        link_text: "View Website",
        popups: "detect",
        state_image_url: "",
        state_image_position: "",
        location_image_url: ""
    },
    state_specific: {
        UZB354: {
            name: "Bukhoro",
            color: region_color,
            hover_color: hover_color,
            id: "#region-bukhara"
        },
        UZB355: {
            name: "Khorezm",
            color: region_color,
            hover_color: hover_color,
            id: "#region-khorezm"
        },
        UZB356: {
            name: "Karakalpakstan",
            color: region_color,
            hover_color: hover_color,
            id: "#region-karakalpakstan"
        },
        UZB357: {
            name: "Navoi",
            color: region_color,
            hover_color: hover_color,
            id: "#region-navoi"
        },
        UZB358: {
            name: "Samarkand",
            color: region_color,
            hover_color: hover_color,
            id: "#region-samarkand"
        },
        UZB361: {
            name: "Kashkadarya",
            color: region_color,
            hover_color: hover_color,
            id: "#region-kashkadarya"
        },
        UZB362: {
            name: "Surkhandarya",
            color: region_color,
            hover_color: hover_color,
            id: "#region-surkhandarya"
        },
        UZB363: {
            name: "Andijan",
            color: region_color,
            hover_color: hover_color,
            id: "#region-andijan"
        },
        UZB364: {
            name: "Ferghana",
            color: region_color,
            hover_color: hover_color,
            id: "#region-fergana"
        },
        UZB365: {
            name: "Namangan",
            color: region_color,
            hover_color: hover_color,
            id: "#region-namangan"
        },
        UZB370: {
            name: "Jizzakh",
            color: region_color,
            hover_color: hover_color,
            id: "#region-jizzakh"
        },
        UZB371: {
            name: "Syrdarya",
            color: region_color,
            hover_color: hover_color,
            id: "#region-syrdarya"
        },
        UZB372: {
            name: "Tashkent",
            color: region_color,
            hover_color: hover_color,
            id: "#region-tashkent"
        },
        UZB4828: {
            name: "Tashkent city",
            color: region_color,
            hover_color: hover_color,
            id: "#region-tashkent-city"
        }
    },
    locations: {},
    labels: {},
    regions: {}
};

