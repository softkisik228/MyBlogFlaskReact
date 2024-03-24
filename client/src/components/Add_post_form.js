import React, { useState} from "react";
import '../css/Add_post_form.css';

const Add_post_form = () => {
    const [show, setShow] = useState(false);
    return (
        <div>
            <button onClick={() => setShow(!show)} className="add-post-btn">{show ? 'Hide' : 'Add post'}</button>
            {show &&<div> <div className="form-box">
                <form className="post-form">
                <textarea type="text" className="text-area" placeholder="Enter the text of the post"></textarea>
                </form>   
            </div>
            <button className="upload-post-btn">Post it</button>
            </div>}
        </div>
    );
}   
export default Add_post_form;