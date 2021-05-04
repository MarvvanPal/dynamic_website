const menuBtn = document.querySelector('.menu-btn');
const menuList = document.querySelector('.burger-menu');
let menuOpen = false;    
menuBtn.addEventListener('click', () => {
        if(!menuOpen) {
            menuBtn.classList.add('open');
            menuList.classList.add('open');
            menuOpen = true;
        } else {
            menuBtn.classList.remove('open');
            menuList.classList.remove('open');
            menuOpen = false;
        }
    });

    function checkForm(form)
    { 
      // regular expression to match only alphanumeric characters and spaces
      var re = /^[\w ]+$/;
  
      // validation fails if the input doesn't match our regular expression
      if((!re.test(form.name.value)) || (!re.test(form.subject.value)) || (!re.test(form.message.value))){
        alert("Error: Input contains invalid characters!");
        form.message.focus();
        return false;
      }

      if((!re.test(form.name.value)) || (!re.test(form.subject.value)) || (!re.test(form.message.value))){
        alert("Error: Input contains invalid characters!");
        form.message.focus();
        return false;
      }
  
      // validation was successful
      //alert("Error: Everything is fine!");
      return true;
    }