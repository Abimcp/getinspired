import React, {useEffect} from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Card, Button } from '../../components';
import { getResult } from '../../actions';

function Main(){
    
    const info = useSelector(state => state.info);
    const loading = useSelector(state => state.loading);
    const error = useSelector(state => state.error)

    const dispatch = useDispatch();
    
    

  

    useEffect(()=>{
        let things = getResult()
        dispatch(things)
    },[])

    
    const renderResult = () => loading ? <p>Loading . . .</p> : <Card info={info}/>

    return (
        <div id="search">
            Would you like to be inspired?
            <Button />
            { error ? <p role="alert" >Oops there's been an error! {error}</p> : renderResult() }
            
        </div>
    );

}

export default Main;
