import './First.css'

function First(){
    const greet = 'Good morning'
    const name = 'Newgen'


    return (
        <>
            <p style={{ backgroundColor:'red'}}>{greet}, {name}</p>
            <p className="first-style">this is print</p>
        </>
    )
}

export default First