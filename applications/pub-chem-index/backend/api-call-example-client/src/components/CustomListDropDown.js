import React from 'react'
export const CustomDropdown = (props) => (
  <div className="form-group">
    <select
      className="form-control"
      name="{syn}"
      onChange={props.onChange}
      id="results"
    >
      <option defaultValue>Select {props.name}</option>
      {props.options.map((item, index) => (
        <option key={index} value={item.id}>
          {item.name}
        </option>
      ))}
    </select>
  </div>
)
export default class CustomListDropDown extends React.Component {
  constructor() {
    super()
    this.state = {
      collection: [],
      selectedValue: '',
      value: '',
    }
  }
  handleSelectChange = (event) => {
    this.setState({ selectedValue: event.target.value })
  }
  handleInputChange = (event) => {
    this.setState({ value: event.target.value })
  }
  handleClick () {
    const radios = document.getElementsByTagName('input');
    // By default is synonyms
    let endpoint = "synonyms";
    for (let i = 0; i < radios.length; i++) {
        if (radios[i].type === 'radio' && radios[i].checked) {
            endpoint = radios[i].value;       
        }
    }
    console.log("Endpoint selected : ", endpoint);

    fetch(`/molecules/${endpoint}/${this.state.value}`)
    .then(response => { return response.json() })
    .then((data) => {
      const options = data.map( item => { return { id : item[0], name: item[1] }})
      this.setState({ collection: options })

      //open drop down
      document.getElementById('results').click()
    })
    .catch((error) => {
      
    })
  }
  render() {
    return (
      <div className="container mt-4">
        <h2>Pubchem search sample React app</h2>
        <input value={this.state.value} onChange={(e) => {this.handleInputChange(e)}} />
        <button onClick={this.handleClick.bind(this)}>Search</button>
        <fieldset>
          <legend>Select a CID Table:</legend>
          <div>
            <input type="radio" id="synonyms" name="cids" value="synonyms" checked/>
            <label for="synonyms">CID-Synonyms</label>
          </div>

          <div>
            <input type="radio" id="mesh" name="cids" value="mesh"/>
            <label for="mesh">CID-Mesh</label>
          </div>

          <div>
            <input type="radio" id="smiles" name="cids" value="smiles"/>
            <label for="smiles">CID-Smiles</label>
          </div>

          <div>
            <input type="radio" id="iupac" name="cids" value="iupac"/>
            <label for="iupac">CID-IUPAC</label>
          </div>

          <div>
            <input type="radio" id="inchi" name="cids" value="inchi"/>
            <label for="inchi">CID-INCHI-Key</label>
          </div>

          <div>
            <input type="radio" id="title" name="cids" value="title"/>
            <label for="title">CID-Titles</label>
          </div>
        </fieldset>
        <CustomDropdown
          options={this.state.collection}
          onChange={this.handleSelectChange}
        />
      </div>
    )
  }
}