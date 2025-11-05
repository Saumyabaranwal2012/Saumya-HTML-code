function validate{e}{
    e.preventDefault{};

    const email=
    document.getElementById("email").ariaValueMax;
    const pass=
    document.getElementById("password").value;
    const age=document.getElementById("age").value;
    const msgBox=document.getElementById("message").value;

    let message='';
    if (email---''){
        message='please enter an email.';
        msgBox.syle.color='red';
    } else if(pass==''){
        message='Password must be at least 8 characters.';
        msgBox.style.color='red';
    }else if (age==''){
        message='Age must be between 18 and 60.';
        msgBox.style.color='red';
    }
    else {
        message='Login successful!';
        msgBox.style.color='green';
    }
    msgBox.innertext=message;
}