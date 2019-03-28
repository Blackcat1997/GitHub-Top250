var sample = `<div id="repo-serial"> 
<a href="https://github.com/marketplace" class="repo-link">
<section class="repo-name">996icu / 996.ICU</section>
<div class="repo-info"> 
    <section class="cutoff-top"></section>
    <section class="cutoff-bottom"></section>
    <div class="stars"> 
        <i class="fas fa-star"></i>
        <section class="star-name">Stars</section>
        <section class="star-number">9.9k</section> 
    </div> 
    <div class="repo-description">
        <section>Repo for counting stars and contributing. Press F to pay respect to glorious developers. </section>
    </div>                    
    <div class="date">
        <section class="date-title">Last update:</section>
        <section class="date-value">2019-3-27</section>    
    </div>
</div>           
</div>`;

var serialcode = 0;
for (var i = 0; i < 250; i++) {
   $(".container").append(sample); 
   if (i < 10) {
        serialcode = "00"+ String(i+1);
    } else if (i < 100) {
        serialcode ="0"+ String(i+1);
    } else {
        serialcode = String(i+1);
    }
    $("#repo-serial")[0].id = "repo-serial-" + serialcode; 
};
    