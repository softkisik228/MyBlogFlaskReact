import React, { useState} from "react";
import '../css/AddPostForm.css';

const AddPostForm = () => {
    const [show, setShow] = useState(false);

    const AddNewPost = () => {
        var post_form = document.getElementById('add-form');
        var today = new Date();
        var dd = String(today.getDate()).padStart(2, '0');
        var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
        var yyyy = today.getFullYear();
        today = dd + '.' + mm + '.' + yyyy;
        try{
            fetch('http://127.0.0.1:5000/add_post?post=' + post_form.post.value + '&date='+ today + '&nickname=kisik');
        }catch (err){
            console.log(err);
        }
        
    }

    return (
        <div>
            <button onClick={() => setShow(!show)} className="add-post-btn">{show ? 'Hide' : 'Add post'}</button>
            {show && <div> <div className="form-box">
                <form className="post-form" id="add-form">
                <textarea type="text" className="text-area" name="post" placeholder="Enter the text of the post"></textarea>
                </form>   
            </div>
            <button onClick={() => AddNewPost()} className="upload-post-btn">Post it</button>
            </div>}
        </div>
    );
}   
export default AddPostForm;