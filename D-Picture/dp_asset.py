asset = """
<!DOCTYPE HTML>
<html>

<head>
    <title>Image Work Area</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="http://127.0.0.1:5555/bootstrap-5.3.3-dist/css/bootstrap.min.css">
    <!-- Fichiers Bootstrap principaux -->
    <link rel="stylesheet" href="http://127.0.0.1:5555/bootstrap-5.3.3-dist/css/bootstrap.css">
    <link rel="stylesheet" href="http://127.0.0.1:5555/bootstrap-5.3.3-dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="http://127.0.0.1:5555/bootstrap-5.3.3-dist/css/bootstrap.rtl.css">
    <link rel="stylesheet" href="bootstrap-5.3.3-dist/css/bootstrap.rtl.min.css">

    <!-- Fichiers pour le système de grille -->
    <link rel="stylesheet" href="http://127.0.0.1:5555/bootstrap-5.3.3-dist/css/bootstrap-grid.css">
    <link rel="stylesheet" href="http://127.0.0.1:5555/bootstrap-5.3.3-dist/css/bootstrap-grid.rtl.css">
    <link rel="stylesheet" href="http://127.0.0.1:5555/bootstrap-5.3.3-dist/css/bootstrap-grid.min.css">
    <link rel="stylesheet" href="http://127.0.0.1:5555/bootstrap-5.3.3-dist/css/bootstrap-grid.rtl.min.css">

    <!-- Fichiers pour les utilitaires -->
    <link rel="stylesheet" href="http://127.0.0.1:5555/bootstrap-5.3.3-dist/css/bootstrap-utilities.css">
    <link rel="stylesheet" href="http://127.0.0.1:5555/bootstrap-5.3.3-dist/css/bootstrap-utilities.rtl.css">
    <link rel="stylesheet" href="http://127.0.0.1:5555/bootstrap-5.3.3-dist/css/bootstrap-utilities.min.css">
    <link rel="stylesheet" href="http://127.0.0.1:5555/bootstrap-5.3.3-dist/css/bootstrap-utilities.rtl.min.css">

    <!-- Fichiers pour le reboot -->
    <link rel="stylesheet" href="http://127.0.0.1:5555/bootstrap-5.3.3-dist/css/bootstrap-reboot.css">
    <link rel="stylesheet" href="http://127.0.0.1:5555/bootstrap-5.3.3-dist/css/bootstrap-reboot.rtl.css">
    <link rel="stylesheet" href="http://127.0.0.1:5555/bootstrap-5.3.3-dist/css/bootstrap-reboot.min.css">
    <link rel="stylesheet" href="http://127.0.0.1:5555/bootstrap-5.3.3-dist/css/bootstrap-reboot.rtl.min.css">

    <script src="http://127.0.0.1:5555/bootstrap-5.3.3-dist/js/bootstrap.min.js"></script>
    <!-- Fichiers JavaScript principaux avec les bundles -->
    <script src="http://127.0.0.1:5555/bootstrap-5.3.3-dist/js/bootstrap.bundle.js"></script>
    <script src="http://127.0.0.1:5555/bootstrap-5.3.3-dist/js/bootstrap.bundle.min.js"></script>

    <!-- Fichiers JavaScript sans les plugins de dépendance -->
    <script src="http://127.0.0.1:5555/bootstrap-5.3.3-dist/js/bootstrap.js"></script>
    <script src="http://127.0.0.1:5555/bootstrap-5.3.3-dist/js/bootstrap.min.js"></script>

    <script src="http://127.0.0.1:5555/jquery/jquery-3.7.1.js"></script>
    <link href="http://127.0.0.1:5555/ressources/util/variables.css">
    <style>
        @import url("http://127.0.0.1:5555/ressources/util/variables.css");

        #image-images {
            width: 100%;
            height: 100%;
            margin: 0;
            padding: 0;
            position: relative;
            overflow: hidden;
            background-color: black;
            user-select: none;
        }

        #ii-container {
            width: 100%;
            height: 100%;
            display: flex;
            flex-wrap: wrap;
            overflow: auto;
            padding: 0;
        }

        #ii-container::-webkit-scrollbar {
            width: 10px;
            height: 10px;
        }

        #ii-container::-webkit-scrollbar-thumb {
            border-radius: 5px;
            background-color: var(--light-color-trans-99);
        }

        #ii-container::-webkit-scrollbar-thumb:hover {
            background-color: var(--light-color-trans-50);
        }

        .iic-img {
            display: flex;
            position: relative;
            overflow: hidden;
            transition: all .5s ease-in-out;
            background-color: black;
            border: 2px solid var(--dark-color);
        }

        .iic-img-2.iici-selected,
        .iic-img-3.iici-selected {
            border: 2px solid var(--dark-purple);
        }

        .iic-img-1.iici-selected {
            border: 2px solid var(--dark-color);
        }

        .iici-img {
            width: 100% !important;
            height: 100% !important;
            max-width: 100% !important;
            max-height: 100% !important;
            min-height: 100% !important;
            min-height: 100% !important;
            object-fit: contain;
        }

        .iic-img-1 {
            width: 100%;
            height: 100%;
            margin: 0;
            position: relative;
            padding: 2px;
            user-select: none;
        }

        .iic-img-2 {
            width: 45%;
            height: 50%;
            min-width: 350px;
            min-height: 200px;
            margin: 20px 2%;
            position: relative;
            display: flex;
            border-radius: 20px;

            .iici-img {
                border-radius: 20px;
                margin: auto auto;
            }
        }

        .iic-img-3 {
            width: 28%;
            height: 35%;
            min-width: 240px;
            min-height: 100px;
            margin: 10px 1.4%;
            position: relative;
            display: flex;
            border-radius: 10px;

            .iici-img {
                border-radius: 10px;
                margin: auto auto;
            }
        }

        .ii-next-prev {
            width: 25px;
            height: 50px;
            padding: 2.5px;
            transition: all .3s;
            cursor: pointer;
            background-color: rgba(128, 128, 128, 0.170);
            position: absolute;
            top: 50%;
            border-radius: 5px;
            transform: translateY(-50%);
        }

        .ii-next-prev:hover {
            background-color: rgba(128, 128, 128, 0.270);
        }

        #ii-prev {
            left: 0;
        }

        #ii-next {
            right: 0;
        }

        #ii-list {
            width: 25px;
            height: 25px;
            position: absolute;
            left: 5px;
            top: 5px;
            cursor: pointer;
            transition: all .3s;
            border-radius: 3px;
            background-color: rgba(128, 128, 128, 0.170);
            filter: drop-shadow(0px 0px 2px var(--dark-color));

            svg {
                position: absolute;
                left: 50%;
                top: 50%;
                transform: translate(-50%, -50%);
            }
        }

        #ii-list:hover {
            box-shadow: 0px 0px 2px var(--light-color);
        }

        .i-svg-hover {
            display: none;
        }

        svg:hover .i-svg-hover {
            display: inline;
        }

        #image-taskbar {
            width: 100%;
            height: 40px;
            position: absolute;
            bottom: 0;
            filter: drop-shadow(0px 0px 3px var(--dark-color));
            z-index: 20;
        }

        .it-wtb {
            width: 25px;
            height: 25px;
            cursor: pointer;
            margin: 7.5px;
            padding: 3px 3px;
            transition: all .3s;
            border-radius: 2px;
            position: relative;

            svg {
                position: absolute;
                left: 50%;
                top: 50%;
                transform: translate(-50%, -50%);
            }

            * {
                transition: all .3s;
            }
        }

        .it-wtb:hover .it-svg-hover {
            display: inline;
        }

        .it-svg-hover {
            display: none;
        }

        #itgm-2,
        #itgm-3 {
            display: none;
        }

        .it-separator {
            width: 2px;
            height: 80%;
            border-radius: 2px;
            background-color: var(--light-color-trans-99);
            margin: auto 10px;
        }

        .it-dtxt {
            margin: auto 10px;
            font-weight: 500;
            user-select: none;
            text-wrap: nowrap;
        }

        #it-title {
            overflow: hidden;
            text-wrap: nowrap;
            text-overflow: ellipsis;
        }

        #image-queu {
            width: 50%;
            min-width: 500px;
            height: 100%;
            position: absolute;
            left: 0;
            top: 0;
            z-index: 10;
            background-color: var(--dark-color-trans-99);
            padding: 0;
            display: none;
        }

        #iq-head {
            width: 100%;
            height: 30px;
            border-bottom: 1px solid var(--light-color-trans-99);
            margin: 0;
            position: relative;
        }

        #iqh-browse {
            display: inline-block;
            padding: 3px 5px;
            border-radius: 3px;
            font-weight: 500;
            cursor: pointer;
            user-select: none;
            transition: all .3s;
            margin: auto 10px;
            background-color: rgba(128, 128, 128, 0.170);
        }

        #iqh-browse:hover {
            background-color: rgba(128, 128, 128, 0.270);
        }

        #iqh-close {
            width: 25px;
            height: 25px;
            border-radius: 3px;
            cursor: pointer;
            padding: 4px;
            transition: all .3s;
            position: absolute;
            top: 50%;
            right: 0;
            transform: translateY(-50%);

            svg {
                position: absolute;
                left: 50%;
                top: 50%;
                transform: translate(-50%, -50%);
            }
        }

        #iqh-close:hover {
            color: var(--light-red);
            filter: drop-shadow(0px 0px 2px var(--light-red));
        }

        #iq-body {
            width: 100%;
            height: calc(100% - 30px - 50px);
            position: relative;
            overflow: auto;
            display: flex;
            flex-wrap: wrap;
        }

        #iq-body::-webkit-scrollbar {
            width: 10px;
            height: 10px;
        }

        #iq-body::-webkit-scrollbar-thumb {
            border-radius: 5px;
            transition: all .3s;
            background-color: var(--light-color-trans-99);
        }

        #iq-body::-webkit-scrollbar-thumb:hover {
            background-color: var(--light-color-trans-50);
        }

        .iqb-container {
            width: clamp(200px, 45%, 500px);
            height: clamp(90px, 35%, 390px);
            border: 2px solid var(--dark-color);
            border-radius: 10px;
            cursor: pointer;
            user-select: none;
            position: relative;
            transition: all .3s;
            overflow: hidden;
            margin: 5px auto;
            display: flex;
            background-color: black;

        }

        .iqbc-selected {
            border: 2px solid var(--dark-blue);
        }

        .iqb-container:hover .iqbc-title {
            bottom: 0;
        }

        .iqb-container:hover .iqbc-img {
            scale: 1.03;
        }

        .iqbc-img {
            width: 100%;
            height: 100%;
            transition: all .3s;
            border-radius: 10px;
            position: relative;
        }

        .iqbc-img img {
            object-fit: cover;
            width: 100%;
            height: 100%;
        }

        .iqbc-title {
            width: calc(100% - 20px);
            max-width: calc(100% - 20px);
            position: absolute;
            bottom: -100%;
            left: 10px;
            overflow: hidden;
            text-wrap: wrap;
            flex-wrap: wrap;
            text-overflow: ellipsis;
            filter: drop-shadow(0px 0px 3px black);
            transition: all .3s;
            padding: 0, 10px 10px 10px;
            text-align: justify;
            font-weight: 600;
        }
    </style>
    <script>
        function sendFile() {
            let files = ["C:/Users/CJ INGENE/Documents/programmation/Project/.Flex/icon.png", "C:/Users/CJ INGENE/Documents/programmation/Project/.Flex/madara.jpg"]; // Exemple
            fetch("http://127.0.0.1:5555/add_files", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ files: files })
            })
                .then(response => response.json())
                .then(data => {
                    console.log("Réponse du serveur :", data)
                    pywebview.api.setUrl();
                })
                .catch(error => console.error("Erreur :", error));
        }
        function setImage(ind) {
            if (ILI.length > 0) {
                if (ind >= ILI.length) {
                    ind = ITSA.lpmod ? 0 : ILI.length - 1;
                }
                if (ind < 0) {
                    ind = ITSA.lpmod ? ILI.length - 1 : 0;
                }
                IICI = ind;
                ICI = ILI[IICI];
                let cur = $("#ii-container").find(`div[cible="${ICI}"]`);
                let tb = $("#iq-body").find(`.iqb-container[cible="${ICI}"]`);
                $(".iic-img").removeClass("iici-selected");
                $(cur).addClass("iici-selected");
                $(".iqb-container").removeClass("iqbc-selected");
                $(tb).addClass("iqbc-selected");
                if (ITSA.gmod === 1) {
                    $(".iic-img").hide().attr("hidden", true);
                    $(cur).attr("hidden", false).show();
                }
                else {
                    let p = $("#ii-container");
                    scrollEl(p, cur)
                }
                $("#it-title").text(ICI);
                $("#it-num").text(IICI + 1 + " / " + ILI.length);
            }
        }
        function scrollEl(parent, child) {
            let pos = $(child).position();
            $(parent).animate({
                scrollTop: pos.top,
                scrollLeft: pos.left
            }, 300);
        }
        function organiseDiv() {
            $(".iic-img").remove();
            $(".iqb-container").remove();
            for (let i = 0; i < ILI.length; i++) {
                let iic = [document.createElement("div"), document.createElement("img")];
                let iqb = [document.createElement("div"), document.createElement("div"),
                document.createElement("img"), document.createElement("div")];
                $(iic[0]).addClass(`iic-img iic-img-${ITSA.gmod}`).attr("cible", ILI[i]);
                $(iic[1]).addClass("iici-img").attr({ "alt": "", "src": ITSA.ilip[ILI[i]] });
                iic[0].appendChild(iic[1]);
                $(iqb[0]).addClass(`iqb-container`).attr("cible", ILI[i]);
                $(iqb[1]).addClass("iqbc-img");
                $(iqb[2]).attr({ "alt": "", "src": ITSA.ilip[ILI[i]] });
                $(iqb[3]).addClass("iqbc-title").text(ILI[i]);
                iqb[1].appendChild(iqb[2]);
                iqb[0].appendChild(iqb[1]);
                iqb[0].appendChild(iqb[3]);
                document.getElementById("ii-container").appendChild(iic[0]);
                document.getElementById("iq-body").appendChild(iqb[0]);
            }
            IICI = ILI.indexOf(ICI);
            setImage(IICI);
            $(".iic-img").on("click", function (e) {
                e.stopImmediatePropagation();
                e.stopPropagation();
                e.preventDefault;
                if (ITSA.gmod === 1) {
                    if ($("#image-taskbar").is(":visible")) {
                        $("#image-taskbar").animate({ bottom: "-50px" }, 200, () => {
                            $("#image-taskbar").attr("hidden", true);
                        })
                    }
                    else {
                        $("#image-taskbar").attr("hidden", false)
                        $("#image-taskbar").animate({ bottom: "0%" }, 200);
                    }
                }
                else {
                    $("#image-taskbar").attr("hidden", false)
                    $("#image-taskbar").animate({ bottom: "0%" }, 200);
                }
                $(".iic-img").removeClass("iici-selected");
                let ind = ILI.indexOf($(this).attr("cible"));
                setImage(ind)
            });
            $(".iqb-container").on("click", function (e) {
                e.stopImmediatePropagation();
                e.stopPropagation();
                e.preventDefault();
                let ind = ILI.indexOf($(this).attr("cible"));
                setImage(ind)
            });
            $("img").on("dragstart", (e) => {
                e.preventDefault();
            });
        };
        function openImageFile() {
            $("#browse").attr({
                type: "file",
                multiple: true,
                accept: ".bmp,.gif,.jpg,.jpeg,.ico,.png,.svg,.tif,.tiff,.webp",
            });
            $("#browse").on("change", function () {
                let files = Array.from(this.files);
                if (files.length > 0) {
                    let fileList = files.map(el => URL.createObjectURL(el));
                    let fileName = files.map(el => el.name);
                    ICI = fileList[0];
                    IICI = 0;
                    ILI = fileName.map(el => el.split("/").pop());
                    ITSA.ilip = {};
                    fileList.forEach(function (el, ind) {
                        ITSA.ilip[ILI[ind]] = el;
                    });
                    organiseDiv();
                }
            });
            $("#browse").click();
            // pywebview.api.openFile().then(respone=>{
            //     if(respone.message){
            //         let get = respone.message;
            //         let fileList = get.split("::");
            //         ICI = fileList[0];
            //         IICI = 0;
            //         ILI = fileList.map(el => el.split("/").pop());
            //         ITSA.ilip = {};
            //         fileList.forEach(function(el, ind){
            //             ITSA.ilip[ILI[ind]] = el;
            //         });
            //         organiseDiv();
            //     }
            // });
        }
        function activeDPMode() {
            let div = document.getElementById("image-images");
            pywebview.api.setFullscreen().then(respone => {
                console.log(respone)
                if (respone.message === true) {
                    div.requestFullscreen().then(() => {
                        if (document.fullscreenElement === div) {
                            ITSA.dpmod = true;
                            IICI -= 1;
                            ITSA.dgmod = ITSA.gmod;
                            ITSA.gmod = 1;
                            let tout = undefined;
                            ITSA.sio = true;
                            function dpmod() {
                                IICI += 1;
                                ICI = ILI[IICI]
                                if (IICI >= ILI.length) {
                                    if (ITSA.lpmod) {
                                        setImage(IICI);
                                    }
                                    else {
                                        desactiveDPMode();
                                    }
                                }
                                organiseDiv();
                                if (ITSA.sio) {
                                    tout = setTimeout(() => {
                                        dpmod();
                                    }, 3000);
                                }
                            }
                            if ($(".ii-next-prev").is(":visible")) {
                                dpmod();
                                console.log("start")
                            }
                            $(".ii-next-prev").hide();
                            $(document).on("fullscreenchange", () => {
                                if (document.fullscreenElement !== div) {
                                    desactiveDPMode();
                                }
                            });
                        }
                    });
                }
                else {
                    desactiveDPMode();
                }
            });

        }
        function desactiveDPMode(tout = undefined) {
            pywebview.api.unsetFullscreen();
            ICI = ILI[IICI];
            clearTimeout(tout);
            ITSA.gmod = ITSA.dgmod;
            ITSA.sio = false;
            organiseDiv();
            $(".ii-next-prev").show();
            $(document).off("fullscreenchange");
            try {
                if (document.fullscreenElement === div) {
                    document.exitFullscreen();
                }
            }
            catch (e) {
                console.log(e);
            }
        }
        var ICI = "";
        var IICI = -1;
        var ILI = [""];
        var ITSA = {
            "gmod": 1,
            "dgmod": 1,
            "sio": false,
            "dpmod": false,
            "lpmod": false,
            "rdmod": false,
            "ilip": {
            },
        }
    </script>
</head>

<body data-bs-theme="dark" style="width: 100%; height: 100%; overflow: hidden;;">
    <div id="div" style="width: 100%; height: 100vh; position: relative">
        <div id="image-images">
            <div id="ii-container">

            </div>
            <wataba class="ii-next-prev" id="ii-prev">
                <svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" fill="currentColor"
                    class="bi bi-caret-left" viewBox="0 0 16 16">
                    <path
                        d="M10 12.796V3.204L4.519 8zm-.659.753-5.48-4.796a1 1 0 0 1 0-1.506l5.48-4.796A1 1 0 0 1 11 3.204v9.592a1 1 0 0 1-1.659.753" />
                    <path class="i-svg-hover"
                        d="m3.86 8.753 5.482 4.796c.646.566 1.658.106 1.658-.753V3.204a1 1 0 0 0-1.659-.753l-5.48 4.796a1 1 0 0 0 0 1.506z" />
                </svg>
            </wataba>
            <wataba class="ii-next-prev" id="ii-next">
                <svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" fill="currentColor"
                    class="bi bi-caret-right" viewBox="0 0 16 16">
                    <path
                        d="M6 12.796V3.204L11.481 8zm.659.753 5.48-4.796a1 1 0 0 0 0-1.506L6.66 2.451C6.011 1.885 5 2.345 5 3.204v9.592a1 1 0 0 0 1.659.753" />
                    <path class="i-svg-hover"
                        d="m12.14 8.753-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z" />
                </svg>
            </wataba>
            <wataba id="ii-list">
                <svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" fill="currentColor"
                    class="bi bi-list" viewBox="0 0 16 16">
                    <path fill-rule="evenodd"
                        d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5" />
                </svg>
            </wataba>
        </div>
        <div id="image-taskbar" class="d-flex flex-row">
            <wataba class="it-wtb" id="it-gmod">
                <svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" fill="currentColor"
                    class="bi bi-square" viewBox="0 0 16 16" id="itgm-1">
                    <path
                        d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2z" />
                    <path class="it-svg-hover"
                        d="M0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2z" />
                </svg>
                <svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" fill="currentColor"
                    class="bi bi-grid" viewBox="0 0 16 16" id="itgm-2">
                    <path
                        d="M1 2.5A1.5 1.5 0 0 1 2.5 1h3A1.5 1.5 0 0 1 7 2.5v3A1.5 1.5 0 0 1 5.5 7h-3A1.5 1.5 0 0 1 1 5.5zM2.5 2a.5.5 0 0 0-.5.5v3a.5.5 0 0 0 .5.5h3a.5.5 0 0 0 .5-.5v-3a.5.5 0 0 0-.5-.5zm6.5.5A1.5 1.5 0 0 1 10.5 1h3A1.5 1.5 0 0 1 15 2.5v3A1.5 1.5 0 0 1 13.5 7h-3A1.5 1.5 0 0 1 9 5.5zm1.5-.5a.5.5 0 0 0-.5.5v3a.5.5 0 0 0 .5.5h3a.5.5 0 0 0 .5-.5v-3a.5.5 0 0 0-.5-.5zM1 10.5A1.5 1.5 0 0 1 2.5 9h3A1.5 1.5 0 0 1 7 10.5v3A1.5 1.5 0 0 1 5.5 15h-3A1.5 1.5 0 0 1 1 13.5zm1.5-.5a.5.5 0 0 0-.5.5v3a.5.5 0 0 0 .5.5h3a.5.5 0 0 0 .5-.5v-3a.5.5 0 0 0-.5-.5zm6.5.5A1.5 1.5 0 0 1 10.5 9h3a1.5 1.5 0 0 1 1.5 1.5v3a1.5 1.5 0 0 1-1.5 1.5h-3A1.5 1.5 0 0 1 9 13.5zm1.5-.5a.5.5 0 0 0-.5.5v3a.5.5 0 0 0 .5.5h3a.5.5 0 0 0 .5-.5v-3a.5.5 0 0 0-.5-.5z" />
                    <path class="it-svg-hover"
                        d="M1 2.5A1.5 1.5 0 0 1 2.5 1h3A1.5 1.5 0 0 1 7 2.5v3A1.5 1.5 0 0 1 5.5 7h-3A1.5 1.5 0 0 1 1 5.5zm8 0A1.5 1.5 0 0 1 10.5 1h3A1.5 1.5 0 0 1 15 2.5v3A1.5 1.5 0 0 1 13.5 7h-3A1.5 1.5 0 0 1 9 5.5zm-8 8A1.5 1.5 0 0 1 2.5 9h3A1.5 1.5 0 0 1 7 10.5v3A1.5 1.5 0 0 1 5.5 15h-3A1.5 1.5 0 0 1 1 13.5zm8 0A1.5 1.5 0 0 1 10.5 9h3a1.5 1.5 0 0 1 1.5 1.5v3a1.5 1.5 0 0 1-1.5 1.5h-3A1.5 1.5 0 0 1 9 13.5z" />
                </svg>
                <svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" fill="currentColor"
                    class="bi bi-grid-3x3-gap" viewBox="0 0 16 16" id="itgm-3">
                    <path
                        d="M4 2v2H2V2zm1 12v-2a1 1 0 0 0-1-1H2a1 1 0 0 0-1 1v2a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1m0-5V7a1 1 0 0 0-1-1H2a1 1 0 0 0-1 1v2a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1m0-5V2a1 1 0 0 0-1-1H2a1 1 0 0 0-1 1v2a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1m5 10v-2a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1v2a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1m0-5V7a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1v2a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1m0-5V2a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1v2a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1M9 2v2H7V2zm5 0v2h-2V2zM4 7v2H2V7zm5 0v2H7V7zm5 0h-2v2h2zM4 12v2H2v-2zm5 0v2H7v-2zm5 0v2h-2v-2zM12 1a1 1 0 0 0-1 1v2a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1zm-1 6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1zm1 4a1 1 0 0 0-1 1v2a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1v-2a1 1 0 0 0-1-1z" />
                    <path class="it-svg-hover"
                        d="M1 2a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1zm5 0a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1zm5 0a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1zM1 7a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1zm5 0a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1zm5 0a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1zM1 12a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1zm5 0a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1zm5 0a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1z" />
                </svg>
            </wataba>
            <div class="it-separator"></div>
            <wataba class="it-wtb" id="it-dpmod">
                <svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" fill="currentColor"
                    class="bi bi-play" viewBox="0 0 16 16">
                    <path
                        d="M10.804 8 5 4.633v6.734zm.792-.696a.802.802 0 0 1 0 1.392l-6.363 3.692C4.713 12.69 4 12.345 4 11.692V4.308c0-.653.713-.998 1.233-.696z" />
                    <path class="i-svg-hover"
                        d="m11.596 8.697-6.363 3.692c-.54.313-1.233-.066-1.233-.697V4.308c0-.63.692-1.01 1.233-.696l6.363 3.692a.802.802 0 0 1 0 1.393" />
                </svg>
            </wataba>
            <wataba class="it-wtb" id="it-lpmod">
                <svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" fill="currentColor"
                    class="bi bi-repeat" viewBox="0 0 16 16">
                    <path
                        d="M11 5.466V4H5a4 4 0 0 0-3.584 5.777.5.5 0 1 1-.896.446A5 5 0 0 1 5 3h6V1.534a.25.25 0 0 1 .41-.192l2.36 1.966c.12.1.12.284 0 .384l-2.36 1.966a.25.25 0 0 1-.41-.192m3.81.086a.5.5 0 0 1 .67.225A5 5 0 0 1 11 13H5v1.466a.25.25 0 0 1-.41.192l-2.36-1.966a.25.25 0 0 1 0-.384l2.36-1.966a.25.25 0 0 1 .41.192V12h6a4 4 0 0 0 3.585-5.777.5.5 0 0 1 .225-.67Z" />
                </svg>
            </wataba>
            <wataba class="it-wtb" id="it-rdmod">
                <svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" fill="currentColor"
                    class="bi bi-shuffle" viewBox="0 0 16 16">
                    <path fill-rule="evenodd"
                        d="M0 3.5A.5.5 0 0 1 .5 3H1c2.202 0 3.827 1.24 4.874 2.418.49.552.865 1.102 1.126 1.532.26-.43.636-.98 1.126-1.532C9.173 4.24 10.798 3 13 3v1c-1.798 0-3.173 1.01-4.126 2.082A9.6 9.6 0 0 0 7.556 8a9.6 9.6 0 0 0 1.317 1.918C9.828 10.99 11.204 12 13 12v1c-2.202 0-3.827-1.24-4.874-2.418A10.6 10.6 0 0 1 7 9.05c-.26.43-.636.98-1.126 1.532C4.827 11.76 3.202 13 1 13H.5a.5.5 0 0 1 0-1H1c1.798 0 3.173-1.01 4.126-2.082A9.6 9.6 0 0 0 6.444 8a9.6 9.6 0 0 0-1.317-1.918C4.172 5.01 2.796 4 1 4H.5a.5.5 0 0 1-.5-.5" />
                    <path
                        d="M13 5.466V1.534a.25.25 0 0 1 .41-.192l2.36 1.966c.12.1.12.284 0 .384l-2.36 1.966a.25.25 0 0 1-.41-.192m0 9v-3.932a.25.25 0 0 1 .41-.192l2.36 1.966c.12.1.12.284 0 .384l-2.36 1.966a.25.25 0 0 1-.41-.192" />
                </svg>
            </wataba>
            <div class="it-separator"></div>
            <div class="it-dtxt" id="it-num">
                0 / 0
            </div>
            <div class="it-dtxt flex-fill" id="it-title">
                
            </div>
        </div>
        <div id="image-queu">
            <div id="iq-head">
                <wataba id="iqh-browse">
                    Browse
                </wataba>
                <wataba id="iqh-close">
                    <svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" fill="currentColor"
                        class="bi bi-x" viewBox="0 0 16 16">
                        <path
                            d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708" />
                    </svg>
                </wataba>
            </div>
            <div id="iq-body">
            </div>
        </div>
        <input type="file" id="browse" hidden>
        <script>
            $(document).ready(() => {
                $("#ii-container").on("click", function (e) {
                    e.stopImmediatePropagation();
                    e.stopPropagation();
                    e.preventDefault();
                    if ($("#image-taskbar").is(":visible")) {
                        $("#image-taskbar").animate({ bottom: "-50px" }, 200, () => {
                            $("#image-taskbar").attr("hidden", true);
                        })
                    }
                    else {
                        $("#image-taskbar").attr("hidden", false)
                        $("#image-taskbar").animate({ bottom: "0%" }, 200);
                    }
                })
                $("img").on("dragstart", (e) => {
                    e.preventDefault();
                });
                $("*").on("contextmenu", (e) => {
                    e.preventDefault();
                });
                $("#ii-prev").on("click", () => {
                    setImage(IICI - 1);
                    //organiseDiv();
                });
                $("#ii-next").on("click", () => {
                    setImage(IICI + 1);
                    //organiseDiv();
                });

                $("#it-gmod").on("click", function (e) {
                    e.stopImmediatePropagation();
                    e.stopPropagation();
                    ITSA.gmod += 1;
                    if (ITSA.gmod > 3) {
                        ITSA.gmod = 1;
                    }
                    $(".iic-img").removeClass("iic-img-1");
                    $(".iic-img").removeClass("iic-img-2");
                    $(".iic-img").removeClass("iic-img-3");
                    $(".iic-img").addClass(`iic-img-${ITSA.gmod}`);
                    $("#it-gmod").find("svg").hide();
                    $(`#itgm-${ITSA.gmod}`).show();
                    if (ITSA.gmod === 1) {
                        $(".iic-img").hide().css("cursor", "default");
                        $("#ii-container").find(`.iic-img[cible="${ICI}"]`).show();

                    }
                    else {
                        $(".iic-img").show().css("cursor", "pointer").attr("hidden", false);
                    }
                    //organiseDiv();
                });
                $("#it-lpmod").on("click", function (e) {
                    e.stopImmediatePropagation();
                    e.stopPropagation();
                    if (ITSA.lpmod === true) {
                        ITSA.lpmod = false;
                        $(this).css({
                            "color": "var(--light-color)",
                            "filter": "drop-shadow(0px 0px 0px)"
                        });
                    }
                    else {
                        ITSA.lpmod = true;
                        $(this).css({
                            "color": "var(--dark-blue)",
                            "filter": "drop-shadow(0px 0px 2px var(--dark-blue))"
                        });
                    }
                });
                $("#it-rdmod").on("click", function (e) {
                    e.stopImmediatePropagation();
                    e.stopPropagation();
                    if (ITSA.rdmod === true) {
                        ITSA.rdmod = false;
                        ILI = ILI.sort();
                        $(this).css({
                            "color": "var(--light-color)",
                            "filter": "drop-shadow(0 0 0)"
                        });
                    }
                    else {
                        for (let i = 0; i < ILI.length; i++) {
                            let j = Math.floor(Math.random() * (i + 1));
                            [ILI[i], ILI[j]] = [ILI[j], ILI[i]];
                        }
                        ITSA.rdmod = true;
                        $(this).css({
                            "color": "var(--dark-blue)",
                            "filter": "drop-shadow(0px 0px 2px var(--dark-blue))"
                        });
                    }
                    organiseDiv();
                });
                var isIqHeadDown = false;
                var iqHeadCoordPoint = [0, 0];
                $("#iq-head").on("mousedown", function (e) {
                    e.stopImmediatePropagation();
                    e.stopPropagation();
                    e.preventDefault();
                    isIqHeadDown = true;
                    iqHeadCoordPoint = [e.offsetX, e.offsetY];
                });
                $(document).on("mouseup mouseleave focusout", () => {
                    isIqHeadDown = false;
                    iqHeadCoordPoint = [0, 0]
                });
                $(document).on("mousemove", function (e) {
                    if (isIqHeadDown) {
                        let x = e.clientX - iqHeadCoordPoint[0];
                        let y = e.clientY - iqHeadCoordPoint[1];

                        let maxX = $(window).width() - $("#image-queu").outerWidth();
                        let maxY = $(window).height() - $("#image-queu").outerHeight();

                        x = Math.max(0, Math.min(x, maxX));
                        y = Math.max(0, Math.min(y, maxY));

                        $("#image-queu").css({ "left": x, "top": y });
                    }
                });
                $("#iqh-close").on("click", function (e) {
                    e.stopPropagation();
                    $("#image-queu").hide();
                });
                $("#ii-list").on("click", function (e) {
                    e.stopPropagation();
                    $("#image-queu").show();
                });

                $("#iqh-browse").on("click", function (e) {
                    e.stopImmediatePropagation();
                    e.stopPropagation();
                    e.preventDefault();
                    openImageFile();
                });
                $("#it-dpmod").on("click", () => {
                    activeDPMode();
                });
                function disableF5(e) { if ((e.which || e.keyCode) == 116) e.preventDefault(); };
                $(document).unbind("keydown", disableF5);
                $(document).off("keydown", disableF5);
                $(document).on("keydown", function (e) {
                    switch (e.key) {
                        case ("ArrowRight"):
                            setImage(IICI + 1);
                            organiseDiv();
                            break;
                        case ("ArrowLeft"):
                            setImage(IICI - 1);
                            organiseDiv();
                            break;
                        //case (" "):
                        //    activeDPMode();
                        //    break;
                    }
                });
            });
        </script>
    </div>
</body>

</html>
"""