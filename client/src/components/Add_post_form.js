import React from "react";
import '../css/Add_post_form.css'

class Add_post_form extends React.Component{
    render(){
        return (
            <div>
                <button className="add-post-btn">Add post</button>
                <div className="form-box">
                    <form className="post-form">
                    <textarea type="text" className="text-area" placeholder="Enter the text of the post"></textarea>
                    </form>   
                </div>
                <button className="upload-post-btn">Post it</button>
            </div>
        ) 
    }
}
export default Add_post_form;