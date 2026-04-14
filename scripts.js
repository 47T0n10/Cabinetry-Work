document.addEventListener('DOMContentLoaded', () => {
    const body = document.body;
    const toggleBtn = document.getElementById('toggleLang');

    // Language Toggle logic
    toggleBtn.addEventListener('click', () => {
        if (body.classList.contains('lang-en')) {
            body.classList.remove('lang-en');
            body.classList.add('lang-fr');
        } else {
            body.classList.remove('lang-fr');
            body.classList.add('lang-en');
        }
    });

    // Gallery population logic (Placeholder for when images are added)
    const gallery = document.getElementById('imageGallery');
    
    // In a real scenario, you'd list files in portfolio/web-optimized
    // For now, we provide instructions for the user.
    const imageList = ["job_001.jpg", "job_002.jpg", "job_003.jpg", "job_004.jpg", "job_005.jpg", "job_006.jpg", "job_007.jpg", "job_008.jpg", "job_009.jpg", "job_010.jpg", "job_011.jpg", "job_012.jpg", "job_013.jpg", "job_014.jpg", "job_015.jpg", "job_016.jpg", "job_017.jpg", "job_018.jpg", "job_019.jpg", "job_020.jpg", "job_021.jpg", "job_022.jpg", "job_023.jpg", "job_024.jpg", "job_025.jpg", "job_026.jpg", "job_027.jpg", "job_028.jpg", "job_029.jpg", "job_030.jpg", "job_031.jpg", "job_032.jpg", "job_033.jpg", "job_034.jpg", "job_035.jpg", "job_036.jpg", "job_037.jpg", "job_038.jpg", "job_039.jpg", "job_040.jpg", "job_041.jpg", "job_042.jpg"]; // Add filenames here like 'job1.jpg', 'job2.jpg'

    if (imageList.length > 0) {
        gallery.innerHTML = '';
        imageList.forEach(imgName => {
            const img = document.createElement('img');
            img.src = `public/images/portfolio/${imgName}`;
            img.className = 'gallery-img';
            img.alt = 'Capital Cabinetry Job Portfolio';
            gallery.appendChild(img);
        });
    }
});
