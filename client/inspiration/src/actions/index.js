import axios from 'axios';

export const loading = () => ({ type: 'LOADING'});

export const loadResult = ( cerise ) => ({ 
    type: 'LOAD_RESULT',
    payload:  cerise  
});

export const getResult = ()=> {
   
    return async dispatch => {
        console.log('clicked')
        dispatch(loading());
        try {
            console.log("trying");
            const newCard = await getNewCard()
            console.log(newCard)
            dispatch(loadResult(newCard))
        } catch (err) {
            console.warn(err.message);
            dispatch({ type: 'SET_ERROR', payload: err.message })
        };
    };
};

export const getNewCard = async () => {
    try {
       const data  = await axios.get(`http://127.0.0.1:8000/generator/`);
       return data.data[0];
    } catch(err) {
        if (data.status === 404) { throw Error('Try again pal!') }
        throw new Error(err.message)
    }
}