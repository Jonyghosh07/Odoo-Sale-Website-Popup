/* ---------------------------------------------
                  Social-Proof
------------------------------------------------ */
var sp_freqency = 11500;
var sp_timeout = 5000;
var popbackup = "";
var details = [];


// set data for the first time
fn_UpdateSocialProofData();
$(".custom-social-proof").stop().slideToggle('slow');

// set interval for popping up/down
var togglevar = setInterval(function () {
  fn_ToggleSocialProof();
}, sp_freqency); //every 14 seconds as defined by sp_freqency var

// set what to do on close
$(".custom-close").click(function () {
  //Stop all timers and hide social proof
  clearTimeout(popbackup);
  clearTimeout(togglevar);
  $(".custom-social-proof").stop().slideToggle('slow');
});




function getData() {
  fetch("/get/proofs")
    .then((res) => res.json())
    .then((json) => (records = json))
    .then(() => {
      for (let i = 0; i < records.length; i++) {
        details.push(records[i]);
      }
    })
}

function fn_UpdateSocialProofData() {
  getData();

  var selecteddetail = details[Math.floor(Math.random(1) * details.length)];

  var customer = (selecteddetail?.cus_name);

  var location = (selecteddetail?.cus_loc);
  var product = (selecteddetail?.prod_name);
  var prodimg = (selecteddetail?.prod_img);

  // $("#sp_customername").text(customer);
  // $("#sp_location").text(location);
  // $("#sp_productname").text(product);



  var purchase_time = new Date(selecteddetail?.sale_datetime);
  var crrnt_time = new Date();

  var diff_as_date = (crrnt_time.getTime() - purchase_time.getTime()) / 1000 ; // this is a time in seconds

  var diff_hours = Math.floor(diff_as_date/ 60 / 60);
  var hours = (diff_hours + " hours ago");
  var sp_time = hours;
  


  if (selecteddetail) {
    var sp_text = '<div class="custom-notification-image-wrapper">\
  <img src="data:image/*;base64,'+ prodimg + '"/>\
  </div>\
  <div class="custom-notification-content-wrapper">\
    <p class="custom-notification-content">\
      <span>'+ customer + '</span> from <span>' + location + '</span> just bought <strong><span>' + product + '</span></strong>\
      <small id="sp_time">'+ sp_time + '</small>\
    </p>\
  </div>';
    document.getElementById("customerdetails").innerHTML = sp_text;
  }

}





function fn_ToggleSocialProof() {
  $(".custom-social-proof").stop().slideToggle('slow', function () {
    // console.log("gone down")
    fn_UpdateSocialProofData();
  });
  //   
  popbackup = setTimeout(function () {
    $(".custom-social-proof").stop().slideToggle('slow');
    // console.log("popped up")
  }, sp_timeout);
}