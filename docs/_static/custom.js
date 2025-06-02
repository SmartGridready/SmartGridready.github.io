document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll('a.external').forEach(function(link) {
        link.setAttribute('target', '_blank');
        link.setAttribute('rel', 'noopener noreferrer');
    });

    document.querySelectorAll("a.reference.external").forEach(function (link) {
        link.setAttribute("target", "_blank");
        link.setAttribute("rel", "noopener noreferrer");
    });
});

document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("img.zoomable").forEach(function (img) {
    // Wrap image in a container
    const wrapper = document.createElement("div");
    wrapper.className = "zoom-wrapper";

    const zoomInBtn = document.createElement("button");
    zoomInBtn.textContent = "+";
    zoomInBtn.className = "zoom-btn zoom-in";

    const zoomOutBtn = document.createElement("button");
    zoomOutBtn.textContent = "–";
    zoomOutBtn.className = "zoom-btn zoom-out";

    const parent = img.parentNode;
    parent.insertBefore(wrapper, img);
    wrapper.appendChild(img);
    wrapper.appendChild(zoomInBtn);
    wrapper.appendChild(zoomOutBtn);

    let scale = 1;

    const updateScale = () => {
      img.style.transform = `scale(${scale})`;
    };

    zoomInBtn.addEventListener("click", () => {
      scale += 0.2;
      updateScale();
    });

    zoomOutBtn.addEventListener("click", () => {
      scale = Math.max(0.2, scale - 0.2);
      updateScale();
    });
  });
});