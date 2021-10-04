import React from 'react';
import { getResult } from '../../actions';
import { useDispatch } from 'react-redux';

const Button = () => {

    const handleSubmit = (e) => {
        console.log(' clicked')
        search()
        e.preventDefault()
    }
    const dispatch = useDispatch();
    
    
    const search = () => {
        dispatch(getResult())
    }

    return (
        <div>
            <button onClick={handleSubmit}>Click me to be inspired</button>
        </div>
    )
}

export default Button